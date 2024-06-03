# Write a function char_freq() that takes a string
# and counts the number of times each character is repeated in it.
# and return the dictionary with the letters as its key.

# Note: Dictionary keys should be placed in alphabetical order.

def char_freq(text):
    num_of_chars = {}
    for char in set(text):
        num_of_chars[char] = text.count(char)
    return dict(sorted(num_of_chars.items()))

