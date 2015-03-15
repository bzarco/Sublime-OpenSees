# OpenSees

OpenSees is a simple plug-in for Sublime Text adding syntax highlighting, code completion, build commands, etc for the [OpenSees][opensees] extension language of [Tcl][tcl] (.tcl).

## Jump to Section

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Updating](#updating)
- [Usage](#usage)
- [Support](#support)
- [License](#license)

## Features

- Support for OpenSees syntax, in addition to Tcl syntax (using default Tcl package)
- Command completion for some Tcl commands (using default Tcl package snippets)
- Run OpenSees scripts (.tcl) using Sequential interpreter without leaving Sublime
- Run OpenSees scripts (.tcl) using Parallel interpreters without leaving Sublime

## Requirements

If first time downloading OpenSees, you will need to [register][openseesRegister] to message board.

#### Windows

- Tcl [*Required*]
    1. Download Tcl from [OpenSees download website][openseesDownload] in order to have compatible version with OpenSees (may need to uninstall previous versions)
    2. Install Tcl (need to change installation path from `C:/Tcl` to `C:/Program Files/Tcl`)
    3. If Sublime Text was running while installing Tcl, it needs to be restarted in order for the plugin to work
- OpenSees [*Required*]
    1. Download OpenSees from [OpenSees download website][openseesDownload]
    2. Locate `OpenSees.exe` in a convenient directory (if using a location different from default `%userprofile%/OpenSees/`, `opensees_dir` or `opensees` settings should be [changed](#configuration))
- MPICH2 [*Optional, only if using OpenSeesParallel*]
    1. Download MPICH2 from [OpenSees parallel download website][openseesParallelDownload] in order to have compatible version with OpenSeesParallel (may need to uninstall previous versions)
    2. Install MPICH2:
        - If you get an error message, you may need to install [.NET Framework 3.5][dotNetFrameworkDownload] first (need 2.0 as of 3/11/2015, but 3.5 works as it includes 2.0 as well)
        - You must be an administrator to install it
        - Make sure installation directory is `%programfiles%/MPICH2/`, if location is different, `mpiexec` setting should be [changed](#configuration)
        - For more information, see [this tutorial][openseesParallelWindowsTutorial]
- OpenSeesParallel (OpenSeesSP, OpenSeesMP) [*Optional*]
    1. Download OpenSeesParallel from [OpenSees parallel download website][openseesParallelDownload]
    2. Locate `OpenSeesSP.exe` and `OpenSeesMP.exe` in a convenient directory (if using a location different from default `%userprofile%/OpenSees/`, `opensees_dir` or `opensees_sp`/`opensees_mp` settings should be [changed](#configuration))

#### Mac OS X

- Tcl [*Required*]
    1. Tcl will most likely be already installed, check current versions to make sure it is compatible with OpenSees (Open `Terminal`, type `tclsh` and then `puts $tcl_version`)
    2. Download Tcl from [OpenSees download website][openseesDownload] in order to have compatible version with OpenSees (may need to uninstall previous versions)
    3. Install Tcl
    4. If Sublime Text was running while installing Tcl, it needs to be restarted in order for the plugin to work
- OpenSees [*Required*]
    1. Download OpenSees from [OpenSees download website][openseesDownload]
    2. Locate `OpenSees` executable in a convenient directory (if using a location different from default `~/OpenSees/`, `opensees_dir` or `opensees` settings should be [changed](#configuration))
- OpenMPI [*Optional, only if using OpenSeesParallel*]
    1. Not needed unless compiling binaries of OpenSeesParallel from source, see below for more information
    2. If compiling from source, download OpenMPI from [OpenMPI Download][openMpiDownload] and install
- OpenSeesParallel (OpenSeesSP, OpenSeesMP) [*Optional*]
    1. As of 3/11/2015, [OpenSees parallel download website][openseesParallelDownload] is not providing binaries for OS X due to the removal of built in OpenMPI, so user will need to [compile the binaries from source][openseesBuild] in order to use OpenSeesSP and OpenSeesMP
    2. After compiling, locate `OpenSeesSP` and `OpenSeesMP` executables in a convenient directory (if using a location different from default `~/OpenSees/`, `opensees_dir` or `opensees_sp`/`opensees_mp` settings should be [changed](#configuration))
    3. OpenSeesParallel has not been tested in OS X yet, if you find any problems please use the [issues portal][issues]

#### Linux

Linux platform has not been tested yet, if you find any problems please use the [issues portal][issues].

[OpenSees download website][openseesDownload] and [OpenSees parallel download website][openseesParallelDownload] do not provide binaries for Linux, so user will need to [compile the binaries from source][openseesBuild] in order to use OpenSees, OpenSeesSP and OpenSeesMP.

If compiling from source, [Tcl][tcl] will be needed for all interpreters and [OpenMPI][openMpiDownload] will be needed for OpenSeesSP and OpenSeesMP. After compiling, locate `OpenSees`, `OpenSeesSP` and `OpenSeesMP` executables in a convenient directory (if using a location different from default `~/OpenSees/`, `opensees_dir` or `opensees`/`opensees_sp`/`opensees_mp` settings should be [changed](#configuration))

Only Tcl and OpenSees are required for running scripts, OpenSeesParallel is optional.

## Installation

#### Using [Package Control][packageControl] (*Recommended*)

For all Sublime Text users it is recommend to install via [Package Control][packageControl].

1. [Install][packageControlInstallation] Package Control if you haven't yet.
2. Use `ctrl+shift+P` (Win, Linux) or `cmd+shift+P` (OS X) then `Package Control: Install Package`
3. Look for `OpenSees` and install it.

#### Manual Install

1. Click the `Preferences > Browse Packages…` menu
2. Browse up a folder and then into the `Installed Packages/` folder
3. Download [zip package][zipPackage], rename it to `OpenSees.sublime-package` and copy it into the `Installed Packages/` directory
4. Restart Sublime Text

## Updating

- If you are using Package Control, updating will be automatic and you don't have to worry about it.
- If using Manual Install, repeat steps [above](#manual-install) and replace `OpenSees.sublime-package` with the new downloaded one.

## Usage

First, make sure [Installation](#installation) steps were completed for your operating system.

#### Running scripts

- With a .tcl script open, press `ctrl+b` (Win, Linux) or `cmd+b` (OS X) to run previously run interpreter (defaults to Sequential)
- To change interpreters, with a .tcl script open, press `ctrl+shift+b` (Win, Linux) or `cmd+shift+b` (OS X) and a popup with all options will appear
- These options are also available using the menu bar: `Tools > Build` and `Tools > Build With...`

#### Configuration

Setting files are parsed with the following priority:

1. Project Settings (.sublime-project, needs to be created/opened using `Project > Save Project As...` and `Project > Open Project`)
2. User Settings (see below)
3. Default Settings (see below)

User and Default settings can be found using Sublime Text menu: `Preferences > Package Settings > OpenSees`

- `Settings - User` is where you change your settings for OpenSees (**make sure you change this file for configuration to persists when plug-in updated**).
- `Settings - Default` is a good reference with detailed descriptions for each setting (**do not modify this file, use User settings for overriding**).

Some important features about the Settings in this plug-in:

- Any string containing `${<var>}` will be expanded to the operating system's enviroment variable (if exists)
- `${<var>}` can also reference to any setting defined in any of the settings files, using `.` separation for accessing nested settings (e.g. `${test.setting}`)
- Settings can be platform specific. Rather than specifying a string path to use, a dictionary is specified. This dictionary may contain the following keys: `windows`, `linux`, and `osx`

## Support

- Any bug or feature request should be reported [here][issues].
- You are welcome to fork and submit pull requests.

## License

All of the source code is available at github [project][home] under the MIT licence:
```
Copyright (c) 2015 Borja Zarco <borja@bzarco.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```


[home]: https://github.com/bzarco/Sublime-OpenSees "Home"
[opensees]: http://opensees.berkeley.edu "OpenSees"
[tcl]: http://www.tcl.tk/ "Tcl"
[openseesDownload]: http://opensees.berkeley.edu/OpenSees/user/download.php "OpenSees Download"
[openseesRegister]: http://opensees.berkeley.edu/community/ucp.php?mode=register "OpenSees Register"
[openseesParallelDownload]: http://opensees.berkeley.edu/OpenSees/parallel/download.php "OpenSees Parallel Download"
[openseesBuild]: http://opensees.berkeley.edu/OpenSees/developer/builds.php "OpenSees Build"
[dotNetFrameworkDownload]: http://www.microsoft.com/en-us/download/details.aspx?id=22 "Dot Net Framework Download"
[openMpiDownload]: http://www.open-mpi.org/software "OpenMPI Download"
[openseesParallelWindowsTutorial]: http://opensees.berkeley.edu/OpenSees/workshops/parallel/Windows.pdf "OpenseesParallel Windows Tutorial"
[packageControl]: https://packagecontrol.io "Package Control"
[packageControlInstallation]: https://packagecontrol.io "Package Control Installation"
[zipPackage]: https://github.com/bzarco/Sublime-OpenSees/archive/master.zip "Zip Package"
[issues]: https://github.com/bzarco/Sublime-OpenSees/issues "Issues"