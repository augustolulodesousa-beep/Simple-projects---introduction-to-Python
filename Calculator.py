while True:
    number_1 = input('Type a number: ')
    number_2 = input('Type the second number: ')
    operator = input('Type the operator: ')
    
    num_1_float = 0
    num_2_float = 0
    valid_numbers = None
  
    try:
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers is None:
        print('One or both typed numbers are invalid')
        continue

    allowed_operators = '+-/*'

    if operator not in allowed_operators:
        print('Invalid operator')
        continue

    if len(operator) > 1:
        print('Type only 1 operator')
        continue

    print('The result is:')
    if operator == '+':
        print(num_1_float + num_2_float)
    elif operator == '-':
        print(num_1_float - num_2_float)
    elif operator == '/':
        print(num_1_float / num_2_float)
    elif operator == '*':
        print(num_1_float * num_2_float)

    exit_program = input('Do you want to quit? [Y]es: ').lower().startswith('y')
    
    if exit_program is True:
        break