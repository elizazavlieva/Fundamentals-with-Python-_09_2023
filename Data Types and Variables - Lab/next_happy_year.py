year = int(input()) + 1

while True:
    current_year = str(year)
    if len(set(current_year)) != len(current_year):
        year += 1
    else:
        print(year)
        break
