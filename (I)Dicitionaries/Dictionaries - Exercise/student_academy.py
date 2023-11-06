def average_students_grades(n):
    average_grade = {}
    student_grade = {}
    for student in range(n):
        name = input()
        grade = float(input())
        if name not in student_grade:
            student_grade[name] = []
            student_grade[name].append(grade)
        else:
            student_grade[name].append(grade)

    for k, v in student_grade.items():
        average = sum(v) / len(v)
        if k not in average_grade and average >= 4.50:
            average_grade[k] = average
    return average_grade


def results(n):
    student = average_students_grades(n)
    for k, v in student.items():
        print(f'{k} -> {v:.2f}')


count = int(input())
results(count)
