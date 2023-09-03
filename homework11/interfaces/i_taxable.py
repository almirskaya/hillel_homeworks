from abc import ABC, abstractmethod


# abstraction
class ITaxable(ABC):
    @abstractmethod
    def calculate_taxes(self):
        pass
