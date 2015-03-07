# OpenSees

OpenSees is a simple plug-in for Sublime Text adding syntax highlighting, code completion, etc for the [OpenSees][opensees] extension language of [Tcl][tcl] (.tcl).

## Jump to Section

- [Features](#features)
- [Installation](#installation)
- [License](#license)

## Features

- Support for OpenSees syntax, in addition to Tcl syntax (using default Tcl package)
- Command completion for some Tcl commands (using default Tcl package snippets)

## Installation

### Using [Package Control][packageControl] (*Recommended*)

For all Sublime Text users it is recommend to install via [Package Control][packageControl].

1. [Install][packageControlInstallation] Package Control if you haven't yet.
2. Use `cmd+shift+P` then `Package Control: Install Package`
3. Look for `OpenSees` and install it.

### Manual Install

1. Click the `Preferences > Browse Packages…` menu
2. Browse up a folder and then into the `Installed Packages/` folder
3. Download [zip package][zipPackage], rename it to `OpenSees.sublime-package` and copy it into the `Installed Packages/` directory
4. Restart Sublime Text

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
[packageControl]: https://packagecontrol.io "Package Control"
[packageControlInstallation]: https://packagecontrol.io "Package Control Installation"
[zipPackage]: https://github.com/bzarco/Sublime-OpenSees/archive/master.zip "Zip Package"