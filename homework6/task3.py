def is_prime(number: int) -> bool:
    if number < 2 or number > 1000:
        return False
    for i in range(2, int(pow(number, 0.5)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = int(input('Enter your number to check if its prime:'))
    if is_prime(num):
        print(f'Number {num} is prime')
    else:
        print(f'Number {num} is not prime')
