pushd ./api-service
    export FLASK_APP=app
    pipenv run python -m flask run
popd
