import os
from random import randrange
from typing import Dict, Any, List
from pycypher.constants import MARK_UNINSTALLED, PLUGINS_PATH
from .plugin_factory import unregister as factory_unregister
from .plugin_factory import instantiate as factory_instantiate
from .plugin_loader import load_plugins as loader_load_plugins

def load_plugins() -> Dict[str,Any]:
    """Load all the available plugins"""
    return loader_load_plugins()

def uninstall(plugin_list: Dict[str,Any], plugin: str) -> None:
    """Unload a plugin module"""
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

def give_me_random_word() -> str:
    words = ["shark","eagle","whale","snake","tiger","lion"]
    return words[randrange(len(words))]
    
def load_cyphers_from_plugins(cyphers_plugin: Dict[str,Any]) -> Dict[str,Any]:
    """Load the available Cyphers based on the installed plugins"""
    result_cyphers: Dict[str, Any] = []
    for cypher_plugin in cyphers_plugin["plugins"]:
        word_to_encrypt = give_me_random_word()
        cypher          = factory_instantiate(cypher_plugin["plugin"].default_init_parameters())
        result_cyphers.append({
            "key": cypher_plugin["key"],
            "name": cypher_plugin["name"],
            "algorithm": cypher.algorithm(),
            "decrypted": word_to_encrypt,
            "encrypted": cypher.encrypt(word_to_encrypt)
        })
    
    return result_cyphers
