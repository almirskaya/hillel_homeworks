from homework10.animal.animal import Animal


class cold_blooded (Animal):
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

    def thermoregulation(self):
        print(f'{self.name} do not have an internal temperature regulation mechanism and are dependent'
              f' on external environmental conditions')

    def bradycardia(self):
        print(f'{self.name} has a slowed heart rate during rest.')

    def bask_in_sunlight(self):
        print(f'{self.name} is basking in the sunlight to acquire vitamin D.')
