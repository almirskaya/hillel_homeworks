from homework10.animal.warm_blooded.birds.birds import Birds


class Peacock (Birds):
    def __init__(self, name, habitat, blood_type, feather_color, tail_length):
        """
        Initialize an Peacock object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            feather_color (str): Represents the color of the bird's feathers.
            tail_length (float): The length of the peacock's tail feathers in meters.

        """
        super().__init__(name, habitat, blood_type, feather_color)
        self.tail_length = tail_length

    def display_feathers(self):
        """
            Simulates the peacock displaying its feathers in courtship rituals.
        """
        print(f'{self.name} is displaying its beautiful feathers in a courtship display.')

    def vocalize(self):
        """
            Simulates the peacock's vocalization.
        """
        print(f'{self.name} is vocalizing with its distinctive call.')

    def long_tail(self):
        """
            Describes the length of the peacock's tail feathers.
        """
        print(f'The tail feathers of {self.name} are {self.tail_length} meters long.')

    def courtship_dance(self):
        """
            Simulates the peacock's courtship dance.
        """
        print(f'{self.name} is performing an elaborate courtship dance to attract a mate.')
