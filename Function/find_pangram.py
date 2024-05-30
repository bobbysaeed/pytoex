# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
# The quick brown fox jumps over the lazy dog.

# Write function is_pangram() to check a sentence to see if it is a pangram or not.
alphabet = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z',
]

def is_pangram(sentence):
    for letter in sentence:
        letter = letter.lower()
        if letter in alphabet:
            alphabet.remove(letter)
        else:
            continue

    if len(alphabet) == 0:
        print('this sentence is a pangram')
    else:
        print('this sentence is Not a pangram')
