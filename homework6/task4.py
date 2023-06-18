import re


def remove_num_in_lines(file_path: str):
    pattern = r'\d+'
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
    for line in lines:
        without_numbers_lines = re.sub(pattern, '', line)
        file.write(without_numbers_lines)
    file.truncate()
