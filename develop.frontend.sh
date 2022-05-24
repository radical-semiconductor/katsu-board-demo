set -e

pushd ./frontend
    export ASPNETCORE_ENVIRONMENT=Development
    dotnet watch
popd
