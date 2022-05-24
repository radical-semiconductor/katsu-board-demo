set -e

pushd ./api-service
    pipenv install
    pipenv graph
    export FLASK_APP=app
    export FLASK_ENV=development
    pipenv run python -m flask run --without-threads --port 8284
popd
