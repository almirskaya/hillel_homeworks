def my_all(iterable):
    for element in iterable:
        if not bool(element):
            return False
    return True


if __name__ == '__main__':
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_of_names = ['Kate', 'Jerry', 'Rick']
    list_of_diff_types = ['Hello, world!', True, False, 20, None]
    empty_list = []
    print(my_all(list_of_numbers))
    print(my_all(list_of_names))
    print(my_all(list_of_diff_types))
    print(my_all(empty_list))
