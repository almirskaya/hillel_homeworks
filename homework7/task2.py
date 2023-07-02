import re


def my_filter(callback, sequence):
    result = []
    for element in sequence:
        if callback(element):
            result.append(element)
    return result


def vowels(word):
    pattern = r'[aeiou]'
    return re.findall(pattern, word, re.IGNORECASE) != []


def is_even(num):
    return num % 2 == 0


def is_positive(num):
    return num > 0


numbers = [-11, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_text = 'Hello, world!'
if __name__ == '__main__':
    filtered_numbers = my_filter(is_even, numbers)
    print(filtered_numbers)

if __name__ == '__main__':
    filtered_num = my_filter(is_positive, numbers)
    print(filtered_num)

if __name__ == '__main__':
    filtered_text = my_filter(vowels, my_text)
    print(filtered_text)
