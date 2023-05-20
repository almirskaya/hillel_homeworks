import re
with open('text.txt', 'r') as file:
    text = file.read()
text = re.sub(r'\.(\w*)\.', r' \g<1> ', text)
text = re.sub(r'(\.{2,5})', r'.', text)
text = re.sub(r'(\s{2})', r' ', text)
text = re.sub(r'(\s{3})', r'.', text)
text = re.sub(r'(\D)(\.+\s*)', r'\g<1>.\n', text)
text = re.sub(r'(\s{2})\.', r'.', text)
list_of_sentences = re.split(r'[.!?]\s', text)
print(list_of_sentences)
