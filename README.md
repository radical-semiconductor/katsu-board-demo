Currently we have only linux instructions and scripts.

Install the .NET6 SDK using instructions provided by your linux distribution.

To check your SDKs:

    $ dotnet --list-sdks
    6.0.102 [/usr/share/dotnet/sdk]

To check your runtimes:

    $ dotnet --list-runtimes
    Microsoft.AspNetCore.App 6.0.2 [/usr/share/dotnet/shared/Microsoft.AspNetCore.App]
    Microsoft.NETCore.App 6.0.2 [/usr/share/dotnet/shared/Microsoft.NETCore.App]

To build the .NET (Blazor) front end and install python dependencies:

    ./build.sh

Currently the assets for the front end are compiled from source, but this could easily be done using CI or other means to remove end user requirement of compiling the .NET code.

To run the demo:

    ./start.sh

To run unit tests run:

    ./test.sh

Then to view, access the local server display by flask:

    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

    http://127.0.0.1:5000/

# Developing on this demo itself
Right now the development cycle is:

- Make change
- Kill server with Ctrl-C
- Rebuild and restart with `./build.sh && ./start.sh`

## Todo
- Make sure server ends when python exits
- Get a TLS echo happening in demo
- Eliminate need for end user to have .NET SDK
- PIPENV_VENV_IN_PROJECT - add ability to debug out python environ
- configure vscode to also use the right linting/venv when editing
- add launchpoints (build, test, start to vscode)
- finish tests for opensslserver
- implement keys

## Questions


## Toolchain automation

    wget https://dot.net/v1/dotnet-install.sh
    chmod +x ./dotnet-install.sh
    source ./dotnet-install.sh -c 6.0 -i ./dotnet