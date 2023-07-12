from homework10.animal.animal import Animal


class warm_blooded (Animal):
    def __init__(self, name, habitat, blood_type):
        """
        Initialize a warm_blooded object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
        """
        super().__init__(name, habitat)
        self.blood_type = blood_type

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def hunt(self, prey: str):
        print(f'{self.name} is hunting on {prey}')

    def communicate(self):
        print(f'{self.name} is communicating')

    def metabolic_rate(self):
        print(f'{self.name} produce and consume more energy to maintain their body temperature.')

    def respiratory_system(self):
        print(f'{self.name} is enable to efficiently break down food and obtain energy')
