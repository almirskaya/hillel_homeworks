class Phone:
    def __init__(self, lines: int, display_type: str, voip_support: bool):
        self.__lines = lines
        self.__display_type = display_type
        self.__voip_support = voip_support

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines_value):
        if type(lines_value) == int and lines_value > 0:
            self.__lines = lines_value
        else:
            raise TypeError("lines_value must be more than 0")

    @property
    def display_type(self):
        return self.__display_type

    @display_type.setter
    def display_type(self, display_value):
        if type(display_value) == str:
            self.__display_type = display_value
        else:
            raise TypeError("display_value must be a str")

    @property
    def voip_support(self):
        return self.__voip_support

    @voip_support.setter
    def voip_support(self, voip_support_value):
        if voip_support_value == bool:
            self.__voip_support = voip_support_value
        else:
            raise ValueError("voip_support_value must be True or False")

    def __str__(self):
        ip_phone = f'{self.__class__.__name__}: {{\n'\
                     f'\tlines:{self.__lines}\n' \
                     f'\tdisplay_type: {self.__display_type}\n' \
                     f'\tvoip_support: {self.__voip_support}\n}}'
        return ip_phone


if __name__ == '__main__':
    Cisco7821 = Phone(4, "LCD", True)
    print(Cisco7821)
