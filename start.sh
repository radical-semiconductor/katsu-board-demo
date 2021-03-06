#!/usr/bin/env bash
set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
export MSYS=winsymlinks:native # required for windows, via Git Bash

case "$OSTYPE" in
  darwin*)  export KATSU_PLATFORM=macos ;;
  linux*)   export KATSU_PLATFORM=linux ;;
  msys*)    export KATSU_PLATFORM=windows ;;
  cygwin*)  export KATSU_PLATFORM=windows ;;
  *)        echo "Platform unsupported: $OSTYPE" && exit 1 ;;
esac

# Get prebuilt frontend-blazor
FRONTEND_ARCHIVE="http://github.com/radical-semiconductor/katsu-board-demo/releases/latest/download/frontend-blazor.tar.gz"
FRONTEND_ARCHIVE_OUTPUT=frontend-blazor-output
if [ ! -d "$FRONTEND_ARCHIVE_OUTPUT" ]; then
    echo Fetching latest release of Frontend Blazor from Radical Semiconductor
    curl --silent --show-error --location $FRONTEND_ARCHIVE | tar zx
fi

# Get prebuilt openssl
OPENSSL_ARCHIVE="http://github.com/radical-semiconductor/katsu-board-demo/releases/latest/download/openssl.$KATSU_PLATFORM.tar.gz"
OPENSSL_ARCHIVE_OUTPUT=openssl-output
if [ ! -d "$OPENSSL_ARCHIVE_OUTPUT" ]; then
    echo Fetching latest release of OpenSSL from Radical Semiconductor
    curl --silent --show-error --location $OPENSSL_ARCHIVE | tar zx
fi

if ! python -m pipx -h  >/dev/null 2>&1; then
    python -m pip install -q --user pipx
fi

pushd $KATSU_PROJECT_ROOT/pykatsu
    python -m pipx run pipenv sync
    python -m pipx run pipenv graph
    export FLASK_APP=pykatsu.api_service.flaskapp
    export FLASK_RUN_PORT=6327
    python -m pipx run pipenv run python -m flask run --without-threads --no-reload --no-debugger
popd
