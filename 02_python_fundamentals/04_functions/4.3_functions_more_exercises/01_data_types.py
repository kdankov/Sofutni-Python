def check_data_type(data_type, value):
    if data_type == 'int':
        return int(value) * 2
    elif data_type == 'real':
        return f'{float(value) * 1.5:.2f}'
    elif data_type == 'string':
        return f'${value}$'
    
input_data_type = input()
input_value = input()

print(check_data_type(input_data_type, input_value))
