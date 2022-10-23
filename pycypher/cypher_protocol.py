
from typing import Protocol
from abc import abstractmethod


class Cypher(Protocol):

    @abstractmethod
    def algorithm(self) -> str:
        raise NotImplementedError
    
    def encrypt(self, word: str) -> str:
        """Encrypt a value"""
    
    def decrypt(self, word: str) -> str:
        """Descrypt a value"""
    
    








