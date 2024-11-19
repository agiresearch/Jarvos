from abc import ABC, abstractmethod


class Memory(ABC):

    @abstractmethod
    def add(self, *args, **kwargs):
        pass

    @abstractmethod
    def query(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete(self, *args, **kwargs):
        pass

    @abstractmethod
    def compress(self, *args, **kwargs):
        pass
