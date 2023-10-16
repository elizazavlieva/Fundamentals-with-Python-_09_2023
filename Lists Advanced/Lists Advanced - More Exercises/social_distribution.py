def wealth(population, min_wealth):
    for index, item in enumerate(population):
        if item < min_wealth:
            diff = min_wealth - item
            wealthiest_part = max(population)
            if wealthiest_part - diff >= min_wealth:
                population[population.index(wealthiest_part)] -= diff
                population[index] += diff
    if len(population) * min_wealth <= sum(population):
        return population

    else:
        return 'No equal distribution possible'


numbers = [int(num) for num in input().split(', ')]
minimum_wealth = int(input())

print(wealth(numbers, minimum_wealth))