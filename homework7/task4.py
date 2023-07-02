def my_max(lst, amount=1):
    if amount <= 0:
        return []
    if amount == 1:
        max_value = lst[0]
        for num in lst:
            if num > max_value:
                max_value = num
        return max_value
    sorted_lst = sorted(lst, reverse=True)
    return sorted_lst[:amount]


def my_min(lst, amount=1):
    if amount <= 0:
        return []
    if amount == 1:
        min_value = lst[0]
        for num in lst:
            if num < min_value:
                min_value = num
        return min_value
    sorted_lst = sorted(lst)
    return sorted_lst[:amount]


numbers = [10, 5, 8, 3, 9, 4, 7, 2, 77, 6, 1, -11, -89, 545]
if __name__ == '__main__':
    max_number = my_max(numbers)
    print(max_number)

if __name__ == '__main__':
    min_number = my_min(numbers)
    print(min_number)

if __name__ == '__main__':
    max_values = my_max(numbers, amount=2)
    print(max_values)

if __name__ == '__main__':
    min_values = my_min(numbers, amount=2)
    print(min_values)
