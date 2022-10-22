import sys
import os
import importlib
import importlib.util as ilu
from typing import Any, List, Dict
from pycypher.constants import EXTERNAL_PACKAGE_LOADING, MARK_UNINSTALLED, PLUGINS_PATH, PLUGINS_SUBFOLDER
from .plugin_factory import register as factory_register


class PluginInterface:
    """Represents a plugin interface"""

    @staticmethod
    def register(factory_register) -> str:
        """Register this plugin in our factory of plugins"""


def import_module_from_external_folder(plugin_file: Dict[str,Any]) -> PluginInterface:
    """Load module from a full path, external folder (not presented as a child package)"""
    spec = importlib.util.spec_from_file_location(
        plugin_file["plugin"], 
        os.path.join(plugin_file["path"],plugin_file["file"])
    )
    plugin = importlib.util.module_from_spec(spec)
    sys.modules[f"{plugin_file['plugin']}"] = plugin
    spec.loader.exec_module(plugin)
    return plugin

def import_module_child_package(plugin_file: Dict[str,Any]) -> PluginInterface:
    """Load module that it is a child package, a subfolder of this one"""
    return importlib.import_module(f"{plugin_file['sub']}.{plugin_file['plugin']}")

def import_module(plugin_file: Dict[str,Any]) -> PluginInterface:
    """Imports a module with the plugin file specification"""
    if EXTERNAL_PACKAGE_LOADING:
       return import_module_from_external_folder(plugin_file)
    return import_module_child_package(plugin_file)

def list_plugins() -> Dict[str, Any]:
    """Load all files presented in the plugins folder"""
    list_files: List[str] = []
    for f in os.listdir(PLUGINS_PATH):
        if os.path.isfile(os.path.join(PLUGINS_PATH,f)):
            if not f".py{MARK_UNINSTALLED}" in f:
                plugin_file = {
                    "plugin": f.replace('.py',''),
                    "file": f,
                    "path": PLUGINS_PATH,
                    "sub": PLUGINS_SUBFOLDER
                } 
                list_files.append(plugin_file)
    return list_files

def load_plugins() -> Dict[str,Any]:
    """Loads all plugins and install them, those not yet installed"""
    plugins_loaded:Dict[str,Any] = {}
    plugins_loaded["plugins"] = []
    for plugin_file in list_plugins():
        plugin      = import_module(plugin_file)      # if a module has already been imported, it's not loaded again, if needed, check reload modules
        plugin_info = plugin.register(factory_register)

        plugins_loaded["plugins"].append({
            "key":plugin_info,
            "name": plugin.__name__,
            "file": plugin.__file__
        })
    print(plugins_loaded)
    return plugins_loaded
