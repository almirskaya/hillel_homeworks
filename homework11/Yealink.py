from phone import Phone
from interfaces.i_taxable import ITaxable


class Yealink(Phone, ITaxable):
    # polymorphism
    def calculate_taxes(self):
        """
        Calculate the taxes for the Yealink phone based on its purchase price.

        Returns:
            float: The calculated taxes for the phone.
        """
        tax_rate = 0.5
        taxes = self.price_for_purchase * tax_rate
        return taxes


if __name__ == "__main__":
    Phone = Yealink("Yealink T54W", True, 199, 1899, "Color LCD",
                  True, False)
    print(f'Your taxes is: {Phone.calculate_taxes()}$')