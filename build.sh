#!/usr/bin/env bash

set -e
pushd ./frontend
    dotnet publish
popd

pushd ./api-service
    pipenv sync
    pipenv graph
popd
