import re

omnivores = {'Monica', 'Fibi', 'Chandler'}
vegetarians = {'Lorry', 'Kate', 'Valery'}
veggies_people = str(omnivores.union(vegetarians))
veggies_people = re.sub("['{}]", "", veggies_people)
print(f'A list of guests who can eat vegetables and herbs: {veggies_people}')