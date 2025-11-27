#Abstraction
from abc import ABC,abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

    
