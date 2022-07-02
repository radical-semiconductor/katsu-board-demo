set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

# Configure
pushd $KATSU_PROJECT_ROOT/liboqs
    if [ ! -d build ]; then
        mkdir -p build
        pushd build
            cmake -GNinja -DCMAKE_INSTALL_PREFIX=$KATSU_PROJECT_ROOT/openssl/oqs ..
        popd
    fi
popd

pushd $KATSU_PROJECT_ROOT/openssl
    if [ ! -f Makefile ]; then
        ./Configure no-shared linux-x86_64 -lm
    fi
popd

# Build loop
while :; do
    pushd $KATSU_PROJECT_ROOT/liboqs
        pushd build
            ninja
            ninja install
        popd
    popd

    pushd $KATSU_PROJECT_ROOT/openssl
        make -j
    popd

    printf "\n### Watching for edits to liboqs and openssl ###\n"
    inotifywait -r -e close_write "$KATSU_PROJECT_ROOT/liboqs" "$KATSU_PROJECT_ROOT/openssl"
done
