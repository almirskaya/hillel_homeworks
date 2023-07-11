from homework10.animal.cold_blooded.fish.fish import Fish


class Guppy (Fish):
    def __init__(self, name, habitat, blood_type, color, tail_size):
        """
        Initialize a Guppy object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            color (str): The color of the fish.
            tail_size (str): The size of the guppy's tail.
        """
        super().__init__(name, habitat, blood_type, color)
        self.tail_size = tail_size

    def display_tail(self):
        """
            Describes the size of the guppy's tail.
        """
        print(f' {self.name} has a {self.tail_size} tail.')
