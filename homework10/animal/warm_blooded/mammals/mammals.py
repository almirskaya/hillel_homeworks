from homework10.animal.warm_blooded.warm_blooded import warm_blooded


class Mammals (warm_blooded):
    def __init__(self, name, habitat, blood_type, covering):
        """
        Initialize a Mammals object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            covering (str): The type of covering, such as 'fur'.
        """
        super().__init__(name, habitat, blood_type)
        self.covering = covering

    def feed_offspring(self):
        # Logic for nursing offspring with milk
        print(f'{self.name} nurse their offspring with milk.')

    def play(self):
        # Add code here to simulate the bear's playful behavior
        print(f'{self.name} is playing and having fun.')
