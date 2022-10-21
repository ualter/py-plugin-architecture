import os
import importlib
from typing import Any, List, Dict
from .cypher_protocol import Cypher
from .plugin_factory import register as factory

PLUGINS_SUBFOLDER = "plugins"
PLUGINS_PATH      = os.path.join(os.getcwd(), __package__,PLUGINS_SUBFOLDER)

class PluginInterface:
    """Represents a plugin interface"""

    @staticmethod
    def register(factory) -> str:
        """Register this plugin in our factory of plugins"""

def import_module(name: str) -> PluginInterface:
    """Imports a module with the given name"""
    return importlib.import_module(name)  

def load_files() -> List[str]:
    """Load all files presented in the plugins folder"""
    list_files: List[str] = []
    for f in os.listdir(PLUGINS_PATH):
        if os.path.isfile(os.path.join(PLUGINS_PATH,f)):
            file_module = f"{__package__}.{PLUGINS_SUBFOLDER}.{f.replace('.py','')}"
            list_files.append(file_module)
    return list_files

def load_plugins() -> Dict[str,Any]:
    """Loads all plugins already installed"""
    plugins_loaded:Dict[str,Any] = {}
    plugins_loaded["plugins"] = []
    for plugin_module in load_files():
        plugin      = import_module(plugin_module)
        plugin_info = plugin.register(factory)

        plugins_loaded["plugins"].append({
            "key":plugin_info,
            "name": plugin.__name__
        })
    return plugins_loaded
