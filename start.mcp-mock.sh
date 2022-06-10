#!/usr/bin/env bash

project_root=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

pushd $project_root/mcp-mock
    pipenv sync
    pipenv run python mcp-mock/mcp.py 1337
popd
