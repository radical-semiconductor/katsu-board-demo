# Katsu Board Demo
## Requirements
### Operating System
**linux**, **OSX**, or **Windows (>=1803)**

For details of **Windows** versions see https://en.wikipedia.org/wiki/Windows_10_version_history

### Python
Please ensure **Python 3.10.X** is installed and on your `PATH`. Please follow the installation instructions reccomended by you operating system vendor. For most **linux** distributions such as **Ubuntu** this means using the system package manage e.g. `apt`, `yum`, `pacman`, etc. On **Windows** and **macOS** using the installer from https://www.python.org/downloads/ should suffice.

### Bash
Any fairly recent version of **linux** or **macOS** should include a new-enough version of `bash`.

On Windows we have tested `bash` provided both by **Windows Subsystem for Linux** (WSL) as well as **Git Bash** aka **Git for Windows**.

See:
- https://docs.microsoft.com/en-us/windows/wsl/install
- https://gitforwindows.org/

## Running the Demo
1. Open up a `bash` prompt and clone this repository using `git`.

       git clone XXXXXX

1. Change directories

       cd katsu-board-demo

1. Run the start script

       ./start.sh

All python and binary runtime dependencies will be installed if missing.

Once you see the following, the app will attempt to open in a browser tab. If it does not, you can manually open the displayed URL.

    Serving frontend-blazor using flask.

    * Running on http://127.0.0.1:6327 (Press CTRL+C to quit)
