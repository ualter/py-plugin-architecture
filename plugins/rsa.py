
import logging
from typing import Dict, Any
from dataclasses import dataclass
from typing import Protocol

log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "rsa"

@dataclass
class RSACypher:

    keysize: int
    version: int
    
    def encrypt(self, word: str) -> None:
        return f"{word} ENCRYPTED in RSA"
    
    def decrypt(self, word: str) -> str:
        return "DECRYPTED"
    
    def algorithm(self) -> str:
        return "RSA"

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, RSACypher)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY

def default_init_parameters() -> Dict[str,Any]:
    return {
      "type": PLUGIN_CYPHER_KEY,
      "keysize": 2048,
      "version": 2
    }



