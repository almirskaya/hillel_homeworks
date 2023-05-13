eleks_employees = ['Monica', 'Fibi', 'Chandler', 'Ross', 'Joe']
toshiba_employees = ['Ross', 'Rass', 'David', 'Joe']
toshiba_employees.extend(eleks_employees)
eleks_employees.clear()
print(eleks_employees)
print(toshiba_employees)
