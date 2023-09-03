def my_map(callback, sequence):
    return [callback(elem) for elem in sequence]


def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    squared_numbers = my_map(square, numbers)
    print(squared_numbers)
