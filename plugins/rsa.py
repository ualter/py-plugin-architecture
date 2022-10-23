
import logging
import rsa
import base64
from typing import Dict, Any, Tuple
from dataclasses import dataclass
from typing import Protocol

log = logging.getLogger(__name__)

PLUGIN_CYPHER_KEY = "rsa"

@dataclass
class RSACypher:

    keysize: int
    version: int
    public_key: Any
    private_key: Any
    
    def encrypt(self, word: str) -> str:
        if not self.private_key:
            pub, priv = self.generate_keys()
            self.public_key = pub
            self.private_key = priv
            
        return base64.b64encode(rsa.encrypt(word.encode(), self.public_key)).decode()
    
    def decrypt(self, word: str) -> str:
        try:
            return rsa.decrypt(base64.b64decode(word), self.private_key).decode()
        except:
            return False
    
    def algorithm(self) -> str:
        return "RSA"
    
    def generate_keys(self) -> Tuple[Any,Any]:
        (publicKey, privateKey) = rsa.newkeys(self.keysize)
        return publicKey, privateKey
    
    def save_generated_keys(publicKey, privateKey) -> None:
        with open('keys/publcKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

def register(factory_register) -> str:
    factory_register(PLUGIN_CYPHER_KEY, RSACypher)
    log.info(f"Registered plugin {PLUGIN_CYPHER_KEY}: {__name__}")
    return PLUGIN_CYPHER_KEY

def default_init_parameters() -> Dict[str,Any]:
    return {
      "type": PLUGIN_CYPHER_KEY,
      "keysize": 512,
      "version": 2,
      "public_key": None,
      "private_key": None,
    }



