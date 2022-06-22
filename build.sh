#!/usr/bin/env bash
set -e

KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

pushd $KATSU_PROJECT_ROOT/frontend
    dotnet publish
popd

pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv sync
    pipenv graph
popd
