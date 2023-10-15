def courses(initial_schedule):
    while True:
        user_input = input().split(':')
        if user_input[0] == 'course start':
            break
        command = user_input[0]
        lesson_title = user_input[1]
        exercise = lesson_title + '-Exercise'
        if command == 'Add':
            if lesson_title not in initial_schedule:
                initial_schedule.append(lesson_title)
        elif command == 'Insert':
            index = int(user_input[2])
            if lesson_title not in initial_schedule:
                initial_schedule.insert(index, lesson_title)
        elif command == 'Remove':
            if lesson_title in initial_schedule:
                initial_schedule.remove(lesson_title)
                if exercise in initial_schedule:
                    initial_schedule.remove(exercise)
        elif command == 'Swap':
            second_lesson_title = user_input[2]
            second_exercise = second_lesson_title + '-Exercise'
            if (lesson_title in initial_schedule) and (second_lesson_title in initial_schedule):
                index_one = initial_schedule.index(lesson_title)
                index_two = initial_schedule.index(second_lesson_title)
                initial_schedule[index_one], initial_schedule[index_two] = \
                    initial_schedule[index_two], initial_schedule[index_one]
                if exercise in initial_schedule and second_exercise in initial_schedule:
                    initial_schedule[index_one + 1], initial_schedule[index_two + 1] = \
                        initial_schedule[index_two + 1], initial_schedule[index_one + 1]
                elif exercise in initial_schedule and second_exercise not in initial_schedule:
                    first = initial_schedule.pop(index_one + 1)
                    initial_schedule.insert(index_two + 1, exercise)
                elif second_exercise in initial_schedule and exercise not in initial_schedule:
                    second = initial_schedule.pop(index_two + 1)
                    initial_schedule.insert(index_one + 1, second)

        elif command == 'Exercise':
            if lesson_title in initial_schedule:
                index = initial_schedule.index(lesson_title)
                if exercise not in initial_schedule:
                    initial_schedule.insert(index + 1, exercise)
            else:
                initial_schedule.append(lesson_title)
                initial_schedule.append(exercise)
    return initial_schedule


first_schedule = input().split(', ')
counter = 1
for item in courses(first_schedule):
    print(f'{counter}.{item}')
    counter += 1
