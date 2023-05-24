import re
all_data = 'name=Amanda=sssss&age=32&&salary=1500&currency=euro'
data = re.findall(r'([^=&]+)=([^&^s{6}(?=)]*)', all_data, flags=0)
dictionary = dict(data)
print(dictionary)
