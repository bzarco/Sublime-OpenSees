import sublime
import sys
from imp import reload

# get all modules of OpenSees present
reload_mods = []
for mod in sys.modules:
    if mod.startswith("OpenSees") and sys.modules[mod] != None:
        reload_mods.append(mod)

# define order of dependencies for proper reloading
mods_load_order = [
    "lib",
    "lib.helpers",

    "commands"
]

# reload modules in order if they were present
for suffix in mods_load_order:
    mod = "OpenSees." + suffix
    if mod in reload_mods:
        reload(sys.modules[mod])