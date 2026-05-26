"""
Create a program that asks the user to type an integer number,
inform whether this number is even or odd. If the user does not type
an integer number, inform that it is not an integer number.
"""
Number = input('Type an integer number: ')

if Number.isdigit():
    number_int = int(Number)
    even = number_int % 2 == 0
    even_text = 'odd'
    
    if even:
        even_text = "even"

    print(f'The number {number_int} is {even_text}')
else:
    print('You did not type an integer number')


"""
Create a program that asks the user for the hour and, based on the time
described, displays the appropriate greeting. Example:
Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
hours = input('Type only the hour: ')

try:
    hours_int = int(hours)
    dawn_hours = hours_int >= 0 and hours_int < 6
    morning_hours = hours_int >= 6 and hours_int < 12
    afternoon_hours = hours_int >= 12 and hours_int < 17
    night_hours = hours_int >= 18 and hours_int <= 23

    if dawn_hours:
        print(f'Good dawn, it is {hours_int} o\'clock!')
    elif morning_hours:
        print(f'Good morning, it is {hours_int} o\'clock!')
    elif afternoon_hours:
        print(f'Good afternoon, it is {hours_int} o\'clock!')
    elif night_hours:
        print(f'Good evening, it is {hours_int} o\'clock!')
    else:
        print('Invalid hour! Type a number between 0 and 23.')
except:
    print('Type only the hour')


"""
Create a program that asks for the user's first name. If the name has 4 letters
or less, write "Your name is short"; if it has between 5 and 6 letters,
write "Your name is normal"; greater than 6 write "Your name is very large".
"""
name = input('Type your name: ')
size = len(name)
small_size = size >= 2 and size <= 4
normal_size = size >= 5 and size <= 6
large_size = size >= 7

if size <= 1:
    print('Type a name.')
elif small_size:
    print(f'Hello {name}, your name is short')
elif normal_size:
    print(f'Hello {name}, your name is normal')
elif large_size:
    print(f'Hello {name}, your name is large')
else:
    print('What did you type to get here?!!')