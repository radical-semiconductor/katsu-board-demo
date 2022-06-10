#!/usr/bin/env bash

pushd ./api-service
    pipenv run python -m pytest
popd
