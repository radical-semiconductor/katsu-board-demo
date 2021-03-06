set -e

export KATSU_PROJECT_ROOT=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

# Build loop, incase you want to clean start dotnet watch. Use CTRL-C in terminal for this
while :; do
    pushd $KATSU_PROJECT_ROOT/frontend
        # As of writing this, dotnet cli has the following quirks:
        # Env variables here don't have an effect when using dotnet watch
        # - Dotnet watch will utilize the default profile in launchSettings.json
        # - You can specify a alternate profile via:
        #   `dotnet watch run --launch-profile=Frontend.Develop`
        #   but then hot reload fails to work.
        # - You can configure the profile to use http only, because
        #   whole app is local....but again, that causes hot reload to stop working
        dotnet watch
    popd
    inotifywait -r -e close_write "$KATSU_PROJECT_ROOT/frontend"
done