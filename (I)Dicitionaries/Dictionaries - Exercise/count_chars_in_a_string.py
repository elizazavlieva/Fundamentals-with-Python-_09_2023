def creating_dictionary(line):
    char_dict = {}
    for item in line:
        if item != " ":
            if item not in char_dict:
                char_dict[item] = 1
            else:
                char_dict[item] += 1
    return char_dict


def result(line):
    char_dictionary = creating_dictionary(line)
    for k, v in char_dictionary.items():
        print(f"{k} -> {v}")


user_input = input()
result(user_input)
