set -e
pushd ./frontend
    dotnet publish
popd

pushd ./api-service
    pipenv install
    pipenv graph
popd
