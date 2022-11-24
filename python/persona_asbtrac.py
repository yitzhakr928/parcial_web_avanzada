from abc import ABC, abstractmethod

class persona(ABC):

    

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def editar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

