import pickle
with open('test/data/list_of_tuples.txt', 'r+b') as file:
    list_of_tuples = pickle.load(file)
for index, item in enumerate(list_of_tuples):
    left_operand = item[0]
    right_operand = item[1]
    operations = item[2]
    result = int
    if operations == 1:
        operations = '+'
        result = left_operand + right_operand
    elif operations == 2:
        operations = '-'
        result = left_operand - right_operand
    elif operations == 3:
        operations = '*'
        result = left_operand * right_operand
    print(f'The result of the "{index+1}" operation: "{left_operand}{operations}{right_operand}={result}"')
