from homework10.animal.cold_blooded.cold_blooded import cold_blooded


class Fish (cold_blooded):
    def __init__(self, name, habitat, blood_type, color):
        """
        Initialize a Fish object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            color (str): The color of the fish.

        """
        super().__init__(name, habitat, blood_type)
        self.color = color

    def swim(self):
        """
            Simulates the swimming behavior of the fish.
        """
        print(f'The {self.name} is swimming gracefully in the water.')

    def breathe_underwater(self):
        """Describes the ability of the fish to breathe underwater."""
        print(f'The {self.name} can breathe underwater using its gills.')

    def change_color(self, new_color):
        """Simulates the ability of some fish to change color."""
        print(f'The {self.name} changes its color to {new_color}')
