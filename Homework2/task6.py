non_unique = ['Monica Dow', 'Fibi Low', 'John Key', 'Monica Dow']
unique_names = dict.fromkeys(non_unique)
unique_names_list = list(unique_names.keys())
print(f'Unique names: {unique_names_list}')
