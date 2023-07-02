divisible_7 = []
for i in range(1, 1001):
    if i % 7 == 0:
        divisible_7.append(i)
print(divisible_7)

# or the following solution

divisible_7 = [number_ for number_ in range(1, 1001) if number_ % 7 == 0]
print(divisible_7)
