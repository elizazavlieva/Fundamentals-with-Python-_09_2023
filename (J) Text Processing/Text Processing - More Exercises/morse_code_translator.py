line = input().split(' | ')
message = ''
morse_letters = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D' ,
                 '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I','.---': 'J', '-.-': 'K', '.-..': 'L',
                 '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
                 '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                 '-.--': 'Y', '--..': 'Z'}

line = [word.split() for word in line]
for words in line:
    for letter in words:
        if letter in morse_letters.keys():
            message += morse_letters[letter]

    message += ' '

print(message)
