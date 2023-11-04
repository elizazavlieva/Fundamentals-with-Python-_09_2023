def solution(n):
    synonym_dict = {}
    for i in range(n):
        word = input()
        synonym = input()
        if word not in synonym_dict:
            synonym_dict[word] = []
        synonym_dict[word].append(synonym)
    return synonym_dict


def printing_synonyms(count):
    dictionary = solution(count)
    for item in dictionary:
        print(f'{item} - {", ".join(dictionary[item])}')


num = int(input())
printing_synonyms(num)
