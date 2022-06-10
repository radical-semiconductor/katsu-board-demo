#!/usr/bin/env bash

pushd ./api-service
    export FLASK_APP=app
    pipenv sync
    pipenv run python -m flask run --without-threads
popd
