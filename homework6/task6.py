import re


def remove_vowels(input_string: str):
    return re.sub(r'[aeiouAEIOU]', '', input_string)


if __name__ == "__main__":
    str_name = 'Hello, world!'
    print(remove_vowels(str_name))
