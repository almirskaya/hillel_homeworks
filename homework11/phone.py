from abc import ABC

from interfaces.i_property import IProperty


# Inheritance
class Phone(IProperty, ABC):
    """The IP Phone class represents a Voice over Internet Protocol (VoIP) phone,also known as an IP phone.
    An IP phone is a hardware-based telephone that uses internet protocol (IP) networks to make and receive phone calls.
    """
    def __init__(self, brand, voip_support, price_for_rent, price_for_purchase, display_type, camera, on_sale):
        """
            Constructor for the Property class.

            Args:
                brand (str): The brand of the property.
                voip_support (bool): Indicates whether the IP phone supports VoIP technology.
                price_for_rent (float): The rental price of the property(monthly).
                price_for_purchase (float): The purchase price of the property.
                display_type (str): The type of display screen (e.g., LCD, touchscreen) used by the phone.
                on_sale (bool): The property is on sale or not.
                camera (bool): The specifies whether the IP phone has a built-in camera for video calls.
            """
        # hiding
        self.__brand = brand
        self.__voip_support = True
        self.__price_for_rent = price_for_rent
        self.__price_for_purchase = price_for_purchase
        self.__display_type = display_type
        self.__on_sale = True
        self.__camera = True
        self.__owner = 'Alice'

    @property
    def brand(self):
        """str: Get the brand or manufacturer of the IP phone."""
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        """Set the brand of the phone."""
        if isinstance(new_brand, str):
            self.__brand = new_brand
        else:
            raise TypeError("Brand should be a string.")

    @property
    def voip_support(self):
        """bool: Check if the phone supports VoIP."""
        return self.__voip_support

    @voip_support.setter
    def voip_support(self, new_voip_support):
        """Set VoIP support status for the phone."""
        if isinstance(new_voip_support, bool):
            self.__voip_support = new_voip_support
        else:
            raise TypeError("VoIP support should be a boolean.")

    @property
    def price_for_rent(self):
        return self.__price_for_rent

    @price_for_rent.setter
    def price_for_rent(self, new_price_for_rent):
        """Set the rental price of the phone (monthly).

        Args:
            new_price_for_rent (float): The new rental price (monthly) in USD.
        """
        if isinstance(new_price_for_rent, (float, int)) and 100 <= new_price_for_rent <= 1000:
            if new_price_for_rent < 200 and new_price_for_rent >= 100:
                # Short-term rental (up to 3 months)
                self.__price_for_rent = new_price_for_rent + 50  # Increase the price
            elif new_price_for_rent >= 200 and new_price_for_rent <= 1000:
                # Long-term rental (3 months to 1 year)
                self.__price_for_rent = new_price_for_rent  # Keep the same price
            else:
                raise ValueError("Price for rent should be between $100 and $1000.")
        else:
            raise ValueError("Price for rent should be a valid number between $100 and $1000.")

    @property
    def price_for_purchase(self):
        """float: Get the purchase price of the phone."""
        return self.__price_for_purchase

    @price_for_purchase.setter
    def price_for_purchase(self, new_price_for_purchase):
        """Set the purchase price of the phone.

        Args:
            new_price_for_purchase (float): The new purchase price in USD.
        """
        if isinstance(new_price_for_purchase, (float, int)) and 200 <= new_price_for_purchase <= 2000:
            if new_price_for_purchase >= 1000:
                # Apply a 10% discount for purchases of $1000 or more
                self.__price_for_purchase = new_price_for_purchase * 0.9
            else:
                self.__price_for_purchase = new_price_for_purchase
        else:
            raise ValueError("Price for purchase should be between $200 and $2000.")

    @property
    def display_type(self):
        """str: Get the type of display used by the phone."""
        return self.__display_type

    @display_type.setter
    def display_type(self, new_display_type):
        """Set the type of display used by the phone.

        Args:
            new_display_type (str): The new display type.
        """
        if isinstance(new_display_type, str):
            self.__display_type = new_display_type
        else:
            raise TypeError("Display type should be a string.")

    @property
    def camera(self):
        """bool: Check if the phone has a camera."""
        return self.__camera

    @camera.setter
    def camera(self, new_camera):
        """Set the presence of a camera in the phone.

        Args:
            new_camera (bool): Indicates if the phone has a camera.
        """
        if isinstance(new_camera, bool):
            self.__camera = new_camera
        else:
            raise TypeError("Camera should be a boolean.")

    @property
    def on_sale(self):
        """bool: Check if the phone is on sale."""
        return self.__on_sale

    @on_sale.setter
    def on_sale(self, new_on_sale):
        """Set the sale status of the phone.

        Args:
            new_on_sale (bool): The new sale status.
        """
        if isinstance(new_on_sale, bool):
            self.__on_sale = new_on_sale
        else:
            raise TypeError("On sale status should be a boolean.")

    @property
    def owner(self):
        """str: Get the owner of the property."""
        return self.owner

    def get_info(self):
        """Display information about the telephone."""
        print(f"Brand: {self.brand}")
        print(f"VoIP Support: {self.voip_support} sq. ft")
        print(f"Price for rent(monthly): {self.price_for_rent}$")
        print(f"Price for purchase: {self.price_for_purchase}$")
        print(f"Display Type: {self.display_type}")
        print(f"Camera: {'Yes' if self.camera else 'No'}")
        print(f"On Sale: {self.on_sale}")
        print(f'Owner is now {self.owner}')
        if self.on_sale:
            print('Property is on sale!')

    # encapsulation
    def buy(self):
        """A thrilling adventure of a buyer and a phone for sale."""
        user_input = input("Welcome to the Phone Emporium! How much are you willing to pay? $")
        try:
            user_input = float(user_input)
        except ValueError:
            raise ValueError("Invalid input. The price should be a numeric value.")

        user_name = input("May I have your name, brave customer? ")
        try:
            if user_name.strip().isalpha():
                print(f"Thank you, {user_name}! Let's embark on this exciting journey!")
        except ValueError:
            raise ValueError("Invalid input. The name should be a string value.")

        price_with_disc = self.__calc_discount()

        if user_input >= self.price_for_purchase and user_input >= price_with_disc:
            print("Congratulations! Your offer is more than acceptable. Let's seal the deal!")
            self.is_sold(user_name)
        elif self.price_for_purchase >= user_input >= price_with_disc:
            print("Hmm, your price is just right.")
            response = input(f"Do you agree to the price of ${user_input} and wish to become the owner of this "
                             f"magnificent phone? (yes/no): ")
            if response.lower() in ["yes", "y", "+"]:
                self.is_sold(user_name)
            else:
                print("You've decided to pass on this adventure. The phone remains available.")
                print(f"The phone's current owner is still {self.owner}")
        elif user_input <= self.price_for_purchase and user_input <= price_with_disc:
            print(f"Sorry, your offer falls short. The lowest I can go is ${price_with_disc}.")
            response = input("Are you willing to accept the price? (yes/no): ")
            if response.lower() in ["yes", "y", "+"]:
                self.is_sold(user_name)
            else:
                print("The deal has fallen through. The phone is still up for grabs.")
                print(f"The phone's current owner is still {self.owner}")
        else:
            raise ValueError("Your offer is not acceptable.")

    def __calc_discount(self):
        """Calculate the price with a thrilling 10% discount."""
        disc = self.__price_for_purchase * 0.1
        price_with_discount = self.__price_for_purchase - disc
        return price_with_discount

    def is_sold(self, user_name):
        """Witness the grand moment when the phone changes ownership."""
        if user_name != 'Alice':
            self.owner = user_name
            self.on_sale = False
            print("Congratulations! You are now the proud owner of this extraordinary phone.")
            print(f"--> The phone's new owner is {self.owner}")
        else:
            print("Wait a minute! You already own this phone.")
            print("The deal has been canceled. The phone is still available.")
            print("You are the phone's rightful owner; don't use this method on yourself.")

    def calculate_taxes(self):
        """Embark on a thrilling tax calculation adventure."""
        tax_rate = 0.5
        taxes = self.__price_for_purchase * tax_rate + 450
        return print(f"You've just uncovered the hidden truth: Your taxes amount to ${taxes}!")

    @owner.setter
    def owner(self, value):
        self.owner = value


if __name__ == "__main__":
    phone = Phone("Yealink T54W", True, 199, 1899, "Color LCD",
                  True, False)
    phone.get_info()
    phone.buy()
    phone.calculate_taxes()
