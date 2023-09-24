choice = int(input('Enter your choice (1/2/3/4): '))

if choice == 1:
    rows_triangle = int(input('Enter the number of rows for the triangle: '))
    up_or_down = input('Enter 'u' for upward or "d" for downward: ')
    if up_or_down == 'u':
        for i in range(1, rows_triangle + 1):
            line = '*' * i
            print(line)
    elif up_or_down == 'd':
        for i in range(rows_triangle, -1, -1):
            line = '*' * i
            print(line)
elif choice == 2:
    rows_rectangle = int(input('Enter the number of rows for the rectangle: '))
    columns_rectangle = int(input('Enter the number of columns for the rectangle: '))
    for i in range(rows_rectangle):
        row = '*' * columns_rectangle
        print(row)
elif choice == 3:
    rows_pyramid = int(input('Enter the number of rows for the pyramid: '))
    for i in range(1, rows_pyramid + 1):
        row = ' ' * (rows_pyramid - i) + '*' * (i * 2 - 1)
        print(row)
elif choice == 4:
    print('Goodbye')
