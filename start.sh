#!/usr/bin/env bash
set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

# Get prebuilt frontend
FRONTEND_ARCHIVE='http://github.com/radical-semiconductor/katsu-board-demo/releases/latest/download/frontend-blazor.tar.gz'
FRONTEND_ARCHIVE_OUTPUT=blazor-frontent-output
if [ ! -d "$FRONTEND_ARCHIVE_OUTPUT" ]; then
    curl --silent --show-error --location $FRONTEND_ARCHIVE | tar zx
fi

pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv sync
    pipenv graph
    export FLASK_APP=pykatsu.api_service.flaskapp
    pipenv run python -m flask run --without-threads
popd
