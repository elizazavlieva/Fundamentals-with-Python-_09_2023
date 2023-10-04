import math

num_of_students = int(input())
course_lectures = int(input())
additional_bonus = int(input())
current_max_bonus = 0
max_attendance = 0
max_bonus = 0

for i in range(num_of_students):
    student_attendance = int(input())
    current_max_bonus = student_attendance / course_lectures * (5 + additional_bonus)
    if current_max_bonus > max_bonus and student_attendance > max_attendance:
        max_bonus = current_max_bonus
        max_attendance = student_attendance
print(f'Max Bonus: {math.ceil(max_bonus)}.')
print(f"The student has attended {max_attendance} lectures.")