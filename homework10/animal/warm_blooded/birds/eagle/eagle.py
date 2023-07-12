from homework10.animal.warm_blooded.birds.birds import Birds


class Eagle (Birds):
    def __init__(self, name, habitat, blood_type, feather_color, wingspan):
        """
        Initialize an Eagle object.

        Args:
            name (str): The name of the animal.
            habitat (str): The habitat where the animal lives.
            blood_type (str): The `blood_type` is used to represent the specific blood type of animal,
                              such as 'Cold-blooded' or 'Warm-blooded'.
            feather_color (str): Represents the color of the bird's feathers.
            wingspan (float): The wingspan of the eagle in meters.
        """
        super().__init__(name, habitat, blood_type, feather_color)
        self.wingspan = wingspan

    def soar(self):
        """
            Simulates the eagle's ability to soar in the sky.
        """
        print(f"{self.name} is soaring high in the sky.")

    def sharp_vision(self):
        """
            Describes the eagle's exceptional vision.
        """
        print(f'{self.name} has excellent vision, allowing it to spot prey from afar.')

    def powerful_talons(self):
        """
            Describes the eagle's powerful talons used for catching and gripping prey.
        """
        print(f'{self.name} has powerful talons that it uses to catch and grip its prey.')

    def territorial(self):
        """
            Describes the eagle's territorial behavior.
        """
        print(f'{self.name} is highly territorial, defending its nesting area from intruders.')
