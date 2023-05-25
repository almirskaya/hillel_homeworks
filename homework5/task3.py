import re
path_of_file = 'text.txt'
with open(path_of_file, 'r') as file:
    all_text = file.read()
letter_counter = {}
for letter in re.findall(r'([Aa-zZ])', all_text.lower(), flags=0):
    if letter in letter_counter:
        letter_counter[letter] += 1
    else:
        letter_counter[letter] = 1
sorted_counter = sorted(letter_counter.items(), key=lambda x: (x[0], x[1]))
for letter, count in sorted_counter:
    print(f'The letter "{letter}" appears "{count}" times in out file ')
