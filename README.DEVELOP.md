# Developing the Katsu Board Demo
## Requirements
First install all of the run requirements in `README.md`, namely `python` and `bash`.

Next install the **.NET6 SDK** using instructions provided by your linux distribution.

To check your SDKs:

    $ dotnet --list-sdks
    6.0.102 [/usr/share/dotnet/sdk]

To check your runtimes:

    $ dotnet --list-runtimes
    Microsoft.AspNetCore.App 6.0.2 [/usr/share/dotnet/shared/Microsoft.AspNetCore.App]
    Microsoft.NETCore.App 6.0.2 [/usr/share/dotnet/shared/Microsoft.NETCore.App]

Additionally you will need to initialize the git submodules

    git submodule update --init --recursive

**liboqs** and **OpenSSL** each have their own build requirements. See:

- https://github.com/radical-semiconductor/liboqs
- https://github.com/radical-semiconductor/openssl


## Standard development
Standard development is done using **Visual Studio Code** (**VSCode**). By default the **Task** `runDevelopment` runs when you open the root folder of the repository. This actively monitors and rebuilds the `api-service`, the `frontend-blazor`, and the `openssl` fork.

To manually launch the live coding **Task**, goto the **Terminal** menu and select **Run Task**, then from the dropdown choose `runDevelopment`.

To manually utilize live reloading without **VSCode**, use the `develop.*` scripts in the root of this repository.

## OpenSSL
OpenSSL is pulled in via git submodules. If you want to incorporate newer versions of the fork, you must pull and commit and new reference as a submodule.

## Frontend Blazor
The blazor frontend is a dotnet wasm application that gets shipped to endusers fully compiled without the need .NET at runtime.

## pykatsu
Flask serves both the api_service and also hosts the wasm static files
the MCP is a python service that communicates between openssl and the katsu board.