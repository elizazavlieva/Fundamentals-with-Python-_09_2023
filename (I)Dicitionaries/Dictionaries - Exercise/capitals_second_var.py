country = input().split(', ')
capital = input().split(', ')

geography_dict = dict(zip(country,capital))

for k, v in geography_dict.items():
    print(f'{k} -> {v}')
