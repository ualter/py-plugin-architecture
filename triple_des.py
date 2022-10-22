
import logging
from dataclasses import dataclass
from typing import Protocol
log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "triple_des"

@dataclass
class TripleDES:

    random_key: str
    
    def encrypt(self, word: str) -> None:
        return f"{word} ENCRYPTED in Triple_DES"
    
    def decrypt(self, word: str) -> str:
        return "DECRYPTED"

    def algorithm(self) -> str:
        return "AES"

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, TripleDES)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY






