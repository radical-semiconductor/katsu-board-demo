set -e

KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv install --dev
    pipenv graph
    export FLASK_APP=pykatsu.api_service.flaskapp
    export FLASK_ENV=development
    pipenv run python -m flask run --without-threads --port 8284
popd
