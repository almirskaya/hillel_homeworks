def even_squares():
    for num in range(0, 1000000001, 2):
        yield num ** 2


my_generation = even_squares()
print(type(my_generation))
for numbers in my_generation:
    print(numbers)
