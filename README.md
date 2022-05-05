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

# Other ideas/todo
## Toolchain automation

    wget https://dot.net/v1/dotnet-install.sh
    chmod +x ./dotnet-install.sh
    source ./dotnet-install.sh -c 6.0 -i ./dotnet