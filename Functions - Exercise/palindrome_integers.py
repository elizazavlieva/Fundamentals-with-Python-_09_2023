def palindrome_integers(list_of_num):
    for i in list_of_num:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


positive_integers = input().split(', ')
palindrome_integers(positive_integers)
