def filtered_palindrome(word):
    if word == word[::-1]:
        return word


words = input().split()
palindrome_word = input()
palindrome_list = [word for word in words if filtered_palindrome(word)]
count = palindrome_list.count(palindrome_word)
print(f'{palindrome_list} \n Found palindrome {count} times')