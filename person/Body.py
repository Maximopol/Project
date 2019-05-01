from abc import ABC, abstractmethod


class Body(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def update(self):
        pass
