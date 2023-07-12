from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, habitat: str):
        """
        Initialize an Animal object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
        """
        self.name = name
        self.habitat = habitat

    @abstractmethod
    def eat(self):
        """
        Simulate the animal is eating.
        """
        pass

    @abstractmethod
    def sleep(self):
        """
        Simulate the animal is sleeping.
        """
        pass

    @abstractmethod
    def hunt(self, prey: str):
        """
        Simulate the animal is hunting.
        """
        pass

    @abstractmethod
    def communicate(self):
        """
        Simulate the animal is communicating with others.
        """
        pass
