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
- Run OpenSees scripts (.tcl) using Sequential interpreter (without exiting Sublime nor needing command window).

## Requirements

If first time downloading OpenSees, you will need to [register][openseesRegister] to message board.

#### Windows

- Tcl
    1. Download Tcl from [OpenSees download website][openseesDownload] in order to have compatible version with OpenSees (may need to uninstall previous versions)
    2. Install Tcl (need to change installation path from `C:/Tcl` to `C:/Program Files/Tcl`)
- OpenSees
    1. Download OpenSees from [OpenSees download website][openseesDownload]
    3. Locate `OpenSees.exe` in a convenient directory (plug-in settings uses `%userprofile%/OpenSees/` as default, but it can be [changed](#configuration))

#### Mac OS X

- Tcl
    1. Tcl will most likely be already installed, check current versions to make sure it is compatible with OpenSees (Open `Terminal`, type `tclsh` and then `puts $tcl_version`)
    2. Download Tcl from [OpenSees download website][openseesDownload] in order to have compatible version with OpenSees (may need to uninstall previous versions)
    3. Install Tcl
- OpenSees
    1. Download OpenSees from [OpenSees download website][openseesDownload]
    3. Locate `OpenSees` executable in a convenient directory (plug-in settings uses `~/OpenSees/` as default, but it can be [changed](#configuration))

#### Linux

TODO

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

#### Running scripts

- With a .tcl script open, press `ctrl+b` (Win, Linux) or `cmd+b` (OS X) to run Sequential interpreter
- This option is also available using the menu bar: `Tools > Build`

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
[packageControl]: https://packagecontrol.io "Package Control"
[packageControlInstallation]: https://packagecontrol.io "Package Control Installation"
[zipPackage]: https://github.com/bzarco/Sublime-OpenSees/archive/master.zip "Zip Package"
[issues]: https://github.com/bzarco/Sublime-OpenSees/issues "Issues"