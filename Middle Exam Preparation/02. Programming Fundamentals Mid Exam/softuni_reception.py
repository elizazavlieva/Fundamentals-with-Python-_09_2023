def working_hours(first_employee,
                  second_employee, third_employee, students):
    hour = 0
    while True:
        if students <= 0:
            break
        students -= (first_employee + second_employee + third_employee)
        hour += 1
        if hour % 4 == 0:
            hour += 1
    return f'Time needed: {hour}h.'


first = int(input())
second = int(input())
third = int(input())
students_count = int(input())
print(working_hours(first, second, third, students_count))