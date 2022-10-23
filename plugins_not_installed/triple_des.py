
import logging
import base64
from dataclasses import dataclass
from typing import Protocol
from typing import Dict, Any
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "triple_des"

@dataclass
class TripleDES:

    random_key: str
    
    def encrypt(self, word: str) -> str:
        while True:
            try:
                key = DES3.adjust_key_parity(get_random_bytes(24))
                break
            except ValueError:
                pass
        cipher = DES3.new(key, DES3.MODE_CFB)
        msg = cipher.iv + cipher.encrypt(str.encode(word))
        return base64.b64encode(msg).decode()
    
    def decrypt(self, word: str) -> str:
        return "DECRYPTED"

    def algorithm(self) -> str:
        return "Triple DES"

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, TripleDES)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY

def default_init_parameters() -> Dict[str,Any]:
    return {
      "type": PLUGIN_CYPHER_KEY,
      "random_key": 512,
    }
