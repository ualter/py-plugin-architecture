
import logging
from dataclasses import dataclass
from typing import Protocol
from typing import Dict, Any
log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "binary"

@dataclass
class Binary:

    def encrypt(self, word: str) -> str:
        result_bin_str = ""
        for w in list(word.encode('ascii')):
            result_bin_str += "{0:b}".format(w) + " "
        return result_bin_str
    
    def decrypt(self, word: str) -> str:
        return "NotImplemented"

    def algorithm(self) -> str:
        return "Binary"

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, Binary)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY

def default_init_parameters() -> Dict[str,Any]:
    return {
      "type": PLUGIN_CYPHER_KEY,
    }
