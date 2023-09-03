from abc import ABC, abstractmethod


# abstraction
class IProperty(ABC):
    """The Property interface represents a generic property."""

    @abstractmethod
    def get_info(self):
        """Get the info of the property."""
        pass

    @abstractmethod
    def buy(self):
        """Buy the property."""
        pass

    @abstractmethod
    def rent(self):
        """Rent the property."""
        pass

    @abstractmethod
    def is_sold(self, owner):
        """Sell the property."""
        pass
