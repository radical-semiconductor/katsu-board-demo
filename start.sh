#!/usr/bin/env bash
set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

# Get prebuilt frontend-blazor
FRONTEND_ARCHIVE='http://github.com/radical-semiconductor/katsu-board-demo/releases/latest/download/frontend-blazor.tar.gz'
FRONTEND_ARCHIVE_OUTPUT=frontend-blazor-output
if [ ! -d "$FRONTEND_ARCHIVE_OUTPUT" ]; then
    curl --silent --show-error --location $FRONTEND_ARCHIVE | tar zx
fi

# Get prebuilt openssl
OPENSSL_ARCHIVE='http://github.com/radical-semiconductor/katsu-board-demo/releases/latest/download/openssl.linux-x86_64.tar.gz'
OPENSSL_ARCHIVE_OUTPUT=openssl-output
if [ ! -d "$OPENSSL_ARCHIVE_OUTPUT" ]; then
    curl --silent --show-error --location $OPENSSL_ARCHIVE | tar zx
fi

if command -v pipenv >/dev/null 2>&1 ; then
    echo "pipenv already installed"
else
    pip install --user pipx
    pipx install pipenv
fi

pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv sync
    pipenv graph
    export FLASK_APP=pykatsu.api_service.flaskapp
    pipenv run python -m flask run --without-threads
popd
