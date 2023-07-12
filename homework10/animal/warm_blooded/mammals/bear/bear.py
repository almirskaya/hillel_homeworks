from homework10.animal.warm_blooded.mammals.mammals import Mammals


class Bear (Mammals):
    def __init__(self, name, habitat, blood_type, covering, predator):
        """
        Initialize a Bear object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            covering (str): The type of covering, such as 'fur'.
            predator (bool): True - predator and False - herbivore.

        """
        super().__init__(name, habitat, blood_type, covering)
        self.predator = predator

    def hunt(self, prey: str) -> object:
        """
            Add code here to simulate the bear's hunting behavior
        """
        print(f'{self.name} started hunting {prey}!')

    def roam(self):
        """
            Add code here to simulate the bear's roaming behavior
        """
        print(f'{self.name} is roaming its territory.')

    def hibernate(self):
        """
            Add code here to simulate the bear's hibernation behavior
        """
        print(f'{self.name} is going into hibernation for the winter.')

    def forage(self):
        """
            Add code here to simulate the bear's foraging behavior
        """
        print(f'{self.name} is searching and gathering food.')

    def is_predator(self):
        """
            Call animal predator or herbivore.
        """
        if self.predator:
            print(f'The{self.name} is predator animal')
        else:
            print(f'The{self.name} is herbivore animal')
