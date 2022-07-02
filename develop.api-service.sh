set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

# Configure
export FLASK_APP=pykatsu.api_service.flaskapp
export FLASK_ENV=development
pushd $KATSU_PROJECT_ROOT/pykatsu
    pipenv install --dev
    pipenv graph
popd

# Build loop, incase you make an edit that crashs flask
while :; do
    pushd $KATSU_PROJECT_ROOT/pykatsu
        pipenv run python -m flask run --without-threads --port 8284 || true
    popd

    printf "\n### Watching for edits to pykatsu ###\n"
    inotifywait -r -e close_write "$KATSU_PROJECT_ROOT/pykatsu"
done