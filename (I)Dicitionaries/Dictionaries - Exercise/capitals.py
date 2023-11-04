country = input().split(', ')
capital = input().split(', ')

geography_dict = {country[i]: capital[i] for i in range(len(capital))}

for k, v in geography_dict.items():
    print(f'{k} -> {v}')
