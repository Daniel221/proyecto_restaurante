from abc import ABC, abstractmethod

class MenuItem(ABC):
    @abstractmethod
    def servir(self):
        raise NotImplementedError

    @abstractmethod
    def get_precio(self):
        raise NotImplementedError

