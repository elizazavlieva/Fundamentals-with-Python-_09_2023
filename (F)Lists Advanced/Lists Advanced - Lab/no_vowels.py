text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
sorted_text = [char for char in text if char.lower() not in vowels]
print(''.join(sorted_text))