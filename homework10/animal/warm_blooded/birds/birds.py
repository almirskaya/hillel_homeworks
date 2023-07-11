from homework10.animal.warm_blooded.warm_blooded import warm_blooded


class Birds (warm_blooded):
    def __init__(self, name, habitat, blood_type, feather_color):
        """
        Initialize a Birds object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            feather_color (str): Represents the color of the bird's feathers
        """
        super().__init__(name, habitat, blood_type)
        self.feather_color = feather_color

    def fly(self):
        """
            Simulates the bird's ability to fly.
        """
        print(f'{self.name} is flying in the sky.')

    def build_nest(self):
        """
            Simulates the behavior of the bird constructing a nest for breeding purposes.
        """
        print(f'{self.name} is building a nest for breeding.')

    def migrate(self):
        """
            Simulates the bird's instinct to migrate to a new habitat.
        """
        print(f'{self.name} is migrating to a new habitat.')

    def sing(self):
        """
            Simulates the bird's ability to produce melodious songs.
        """
        print(f'{self.name} is singing a beautiful song.')

    def camouflage(self):
        """
            Simulates the bird's ability to camouflage itself to blend into the surroundings.
        """
        print(f'{self.name} is camouflaging itself to blend into the surroundings.')
