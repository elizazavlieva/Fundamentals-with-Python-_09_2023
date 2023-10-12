def sorting_names(names):
    return sorted(names, key=lambda x: (-len(x), x))


name_list = input().split(', ')
print(sorting_names(name_list))