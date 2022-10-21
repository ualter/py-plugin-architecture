
from dataclasses import dataclass
from typing import Protocol

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

def register(factory) -> str:
    factory(PLUGIN_CYPHER_KEY, RSACypher)
    print(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY




