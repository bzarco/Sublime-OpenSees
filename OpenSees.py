import sublime
import os

installed_dir = __name__.split(".")[0]

# only allow ST3
if not (sublime.version() == "" or int(sublime.version()) > 3000):
    sublime.error_message(u"OpenSees\n\nThis package only works with Sublime Text 3, please upgrade.")

# make sure OpenSees was installed properly
elif installed_dir != "OpenSees":
    message = (u"OpenSees\n\nThis package appears to be installed " +
        u"incorrectly.\n\nIt should be installed as \"OpenSees\", " +
        u"but seems to be installed as \"%s\".\n\n" % installed_dir)
    # if installed unpacked
    if os.path.exists(os.path.join(sublime.packages_path(), installed_dir)):
        message += (u"Please use the Preferences > Browse Packages... menu " +
            u"entry to open the \"Packages/\" folder and rename" +
            u"\"%s/\" to \"OpenSees/\" " % installed_dir)
    # if installed as a .sublime-package file
    else:
        message += (u"Please use the Preferences > Browse Packages... menu " +
            u"entry to open the \"Packages/\" folder, then browse up a " +
            u"folder and into the \"Installed Packages/\" folder.\n\n" +
            u"Inside of \"Installed Packages/\", rename " +
            u"\"%s.sublime-package\" to " % installed_dir +
            u"\"OpenSees.sublime-package\" ")
    message += u"and restart Sublime Text."
    sublime.error_message(message)

# package is installed correctly, finish setting up
else:

    # make sure all dependencies are reloaded on upgrade
    import sys
    from imp import reload
    reloader_name = "OpenSees.lib.reloader"
    if reloader_name in sys.modules:
        reload(sys.modules[reloader_name])

    # import reloader for automatic reload of files
    from .lib import reloader

    # register all commands
    from .commands import *

    # define plugin_loaded method to run when the plugin is ready
    def plugin_loaded():
        pass

    # define plugin_unloaded method to run when the plugin is uninstalled
    def plugin_unloaded():
        pass