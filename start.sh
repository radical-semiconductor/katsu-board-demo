#!/usr/bin/env bash

KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

pushd $KATSU_PROJECT_ROOT/pykatsu
    export FLASK_APP=pykatsu.api_service.flaskapp
    pipenv run python -m flask run --without-threads
popd
