"""
Looping through a string using while
"""
#       0123456
name = 'Augusto'  
#       7654321
letter = len(name)
name_size = 0
new_name = ''

while name_size < len(name):
    letter = name[name_size]
    new_name += f'*{letter}'
    name_size += 1

new_name += '*'
print(new_name)