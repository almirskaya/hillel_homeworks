elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_index = []
even_index = []
for element in elements:
    print(element)
for index, value in enumerate(elements):
    if not index % 2 == 0:
        odd_index.append((index, value))
    else:
        even_index.append((index, value))
print(f'The numbers with odd index: {odd_index}')
print(f'The numbers with even index: {even_index}')
