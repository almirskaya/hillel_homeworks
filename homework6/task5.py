def sum_args(*args: int):
    return sum(args)


if __name__ == "__main__":
    result = sum_args(524, 420, 56985, 41, 12, 85)
print(f'Sum of the args is {result}')
