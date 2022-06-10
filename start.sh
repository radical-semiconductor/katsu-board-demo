#!/usr/bin/env bash

pushd ./api-service
    export FLASK_APP=app
    pipenv run python -m flask run --without-threads
popd
