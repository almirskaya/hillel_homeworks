import re

casino_blacklist = {"Kate Moss", "Liza Fin", "Liza Nope", "Richard Row"}
poker_blacklist = {"Richard Row", "Liza Nope", "Ricky Martin"}
alcohol_blacklist = {"Ricky Martin", "Kate Moss", "Richard Row", "Liza Nope"}

names = str(casino_blacklist.intersection(poker_blacklist, alcohol_blacklist))
names = re.sub("[{}']", "", names)
print(f'Persons, who are on all blacklists: {names}')
