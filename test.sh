#!/usr/bin/env bash

pushd ./api-service
    pipenv sync
    pipenv run python -m pytest
popd
