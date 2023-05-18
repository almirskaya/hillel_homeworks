import re
camel_case_vars = ['FirstItem', 'FriendsList', 'MyTuple']
snake_case_vars = [re.sub(r'(?<!^)(?=[A-Z])', '_', elements).lower() for elements in camel_case_vars]
print(snake_case_vars)
