def company():
    companies = {}
    while True:
        command = input()
        if command == 'End':
            break
        company_name, employee_id = command.split(' -> ')
        if company_name not in companies:
            companies[company_name] = []
            companies[company_name].append(employee_id)
        else:
            if employee_id not in companies[company_name]:
                companies[company_name].append(employee_id)
    return companies


def results():
    result = company()
    for k, v in result.items():
        print(f'{k}')
        for i in v:
            print(f'-- {i}')


results()
