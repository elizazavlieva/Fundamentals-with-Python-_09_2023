students = []
searched_course = ''
while True:
    user_input = input()

    if ':' not in user_input:
        searched_course = user_input
        break

    name, id_num, course = user_input.split(':')
    students.append({'name': name, 'ID': id_num, 'course': course})

for student in students:
    if searched_course.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['ID']}")
