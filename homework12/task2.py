import random


class Wagon:
    """Represents a wagon in a train."""

    def __init__(self, number):
        """
        Initialize a wagon with a given number.

        Args:
            number (int): The number of the wagon.
        """
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        """
        Add a passenger to the wagon.

        Args:
            passenger: The passenger to add.

        Note:
            Only allows adding passengers if the wagon is not already full.
            The wagon can hold a maximum of 10 passengers.
        """
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print(f"Wagon {self.number} is already full. Cannot add more passengers.")

    def __len__(self):
        """
        Get the number of passengers in the wagon.

        Returns:
            int: The number of passengers.
        """
        return len(self.passengers)

    def __repr__(self):
        """
        Get the string representation of the wagon.

        Returns:
            str: The string representation of the wagon.
        """
        return f"[{self.number}]"


class Train:
    """Represents a train composed of wagons."""

    def __init__(self):
        """Initialize an empty train."""
        self.wagons = []
        self.locomotive = None

    def add_wagon(self, wagon):
        """
        Add a wagon to the train.

        Args:
            wagon (Wagon): The wagon to add.

        Note:
            If the locomotive has not been set, the added wagon becomes the locomotive.
            Otherwise, the wagon is appended to the list of wagons.
        """
        if self.locomotive is None:
            self.locomotive = wagon
        else:
            self.wagons.append(wagon)

    def __len__(self):
        """
        Get the number of wagons in the train.

        Returns:
            int: The number of wagons (excluding the locomotive).
        """
        return len(self.wagons)

    def __repr__(self):
        """
        Get the string representation of the train.

        Returns:
            str: The string representation of the train.
        """
        wagon_str = "-".join([str(wagon) for wagon in self.wagons[::-1]])
        return f"<=[HEAD]-{wagon_str}"


if __name__ == "__main__":
    wagons = [Wagon(i) for i in range(1, 9)]

    for i, wagon in enumerate(wagons):
        num_passengers = random.randint(1, 15)
        for j in range(num_passengers):
            wagon.add_passenger(f"Passenger {i * 25 + j + 1}")

    train = Train()
    for wagon in wagons:
        train.add_wagon(wagon)

    print(train)
