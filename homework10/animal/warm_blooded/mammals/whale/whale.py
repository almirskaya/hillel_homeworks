from homework10.animal.warm_blooded.mammals.mammals import Mammals


class Whale (Mammals):
    def __init__(self, name, habitat, blood_type, covering, dive_depth):
        """
        Initialize a Whale object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            covering (str): The type of covering, such as 'fur'.
            dive_depth (int): Represents the maximum depth at which the whale can dive, in metres.
        """
        super().__init__(name, habitat, blood_type, covering)
        self.dive_depth = dive_depth

    def breach(self):
        """
        Simulate the behavior of whale breaching out of the water.
        """
        print(f'{self.name} is breaching out of the water!')

    def teach_calves(self):
        """
        Simulate the behavior of orcas teaching their calves.
        """
        print(f'{self.name} is teaching its calves.')

    def socialize(self, whale: str):
        """
        Simulate the social behavior of orcas.
        """
        print(f'{self.name} is socializing with {whale}.')

    def sing(self):
        print(f'{self.name} is singing a beautiful whale song.')
