

# local imports to keep things neat
from sys import modules
import importlib

global PRELOADED_MODULES

# sys and importlib are ignored here too
PRELOADED_MODULES = set(modules.values())

def package_reload() :
    from sys import modules
    import importlib

    for module in set(modules.values()) - PRELOADED_MODULES:
        try:
            importlib.reload(module)
        except :
            # there are some problems that are swept under the rug here
            pass