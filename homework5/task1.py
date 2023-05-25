import os
import pickle
import random
list_of_tuples = []
for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operations = random.randint(1, 3)
    list_of_tuples.append((left_operand, right_operand, operations))
os.makedirs("test/data", exist_ok=True)
with open('test/data/list_of_tuples.txt', 'w+b') as file:
    pickle.dump(list_of_tuples, file)
