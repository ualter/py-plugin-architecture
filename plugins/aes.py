
import logging
import base64
from dataclasses import dataclass
from typing import Dict,Any
from Crypto.Cipher import AES
log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "aes"

@dataclass
class AESCypher:

    random_32_key: str
    
    def encrypt(self, word: str) -> str:
        key = str.encode(self.random_32_key)
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(str.encode(word))
        return base64.b64encode(ciphertext).decode()
    
    def decrypt(self, word: str) -> str:
        return "NotImplemented"

    def algorithm(self) -> str:
        return "AES"

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, AESCypher)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY

def default_init_parameters() -> Dict[str,Any]:
    return {
      "type": PLUGIN_CYPHER_KEY,
      "random_32_key": "Sixteen byte keySixteen byte key"
    }






