from homework10.animal.cold_blooded.fish.fish import Fish


class Salmon (Fish):
    def __init__(self, name, habitat, blood_type, color, migratory):
        """
        Initialize a Salmon object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            color (str): The color of the fish.
            migratory (bool): Indicates whether the salmon is migratory or not.
        """
        super().__init__(name, habitat, blood_type, color)
        self.migratory = migratory

    def migrate(self):
        """
            Simulates the migratory behavior of salmon.
        """
        if self.migratory:
            print(f'The {self.name} is migrating upstream to spawn.')
        else:
            print(f'The {self.name} does not migrate.')
