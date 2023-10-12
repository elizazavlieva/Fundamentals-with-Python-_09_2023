def employee_happiness():
    happiness_list = list(map(int, input().split()))
    factor = int(input())
    improved_happiness = [happy * factor for happy in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)
    message = 'happy' if count >= total_count / 2 else 'not happy'
    result = f'Score: {count}/{total_count}. Employees are {message}!'
    return result


print(employee_happiness())