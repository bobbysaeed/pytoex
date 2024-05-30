def is_palindrome(word):
    list_of_letters = []
    [list_of_letters.append(letter) for letter in word]
    new_word = list_of_letters[::-1]
    new_word = (''.join(new_word))
    if new_word == word:
        print(True)
    else:
        print(False)