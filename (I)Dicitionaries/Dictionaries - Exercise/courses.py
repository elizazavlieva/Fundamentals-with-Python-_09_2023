def solution():

    total_registered_users = {}
    while True:
        command = input()
        if command == 'end':
            break
        course, student_name = command.split(' : ')
        if course not in total_registered_users:
            total_registered_users[course] = []
            total_registered_users[course].append(student_name)
        else:
            total_registered_users[course].append(student_name)

    return total_registered_users


def result():
    courses = solution()
    for k, v in courses.items():
        print(f'{k}: {len(courses[k])}')
        for student in v:
            print(f'-- {student}')


result()
