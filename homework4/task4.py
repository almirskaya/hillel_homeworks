import re
with open('index.html', 'r') as f:
    html_file = f.read()
change_code = re.findall(r'<div\s+id="(?P<id>[^"]+)">\s*<a\s+href="(?P<href>[^"]+)">\s*(?P<text>[^<]+)\s*</a>',
                         html_file, flags=0)
result = []
for elements in change_code:
    result.append((elements[0], elements[1], elements[2].strip()))
print(result)
