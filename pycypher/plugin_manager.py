import os
from typing import Dict, Any, List
from pycypher.constants import MARK_UNINSTALLED, PLUGINS_PATH
from .plugin_factory import unregister as factory_unregister
from .plugin_loader import load_plugins as loader_load_plugins

def load_plugins() -> Dict[str,Any]:
    return loader_load_plugins()

def uninstall(plugin_list: Dict[str,Any], plugin: str) -> None:
    plugin_to_unregister = next(p for p in plugin_list["plugins"] if p["key"] == plugin)
    factory_unregister(plugin_to_unregister["key"])
    os.rename(plugin_to_unregister["file"],plugin_to_unregister["file"]+MARK_UNINSTALLED)

def install_plugin(file):
    try:
        contents = file.file.read()
        target_file = os.path.join(PLUGINS_PATH,file.filename)
        with open(target_file, 'wb') as f:
            f.write(contents)
    except Exception:
        raise Exception
    finally:
        file.file.close()

