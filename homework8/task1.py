def print_function_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Function was called : {func.__name__}')
        return result
    return wrapper


@print_function_name
def adding(a, b):
    return a + b


@print_function_name
def multiply(a, b):
    return a * b


number_1 = int(input('Enter number 1:'))
number_2 = int(input('Enter number 2:'))
print(f'Result of the adding of {number_1} and {number_2} =', adding(number_1, number_2))
print(f'Result of the multiply of {number_1} and {number_2} =', multiply(number_1, number_2))
