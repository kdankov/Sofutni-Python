current_line = input()

companies_dict = {}

while current_line != 'End':
    args = current_line.split(' -> ')
    company_name = args[0]
    emplyee_id = args[1]
    
    if company_name not in companies_dict:
        companies_dict[company_name] = []
        
    if emplyee_id not in companies_dict[company_name]:
        companies_dict[company_name].append(emplyee_id)
    
    current_line = input()
    
for key, value in companies_dict.items():
    print(key)
    for i in range(len(value)):
        print(f'-- {value[i]}')