#!/usr/bin/env bash

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv run python -m pytest
popd
