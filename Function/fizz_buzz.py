# Write a function that takes two arguments,
# fizz, buzz; when called,
# it prints the numbers from 1 to 100 inclusive.

# But for multiples of fizz print “Fizz” instead of the number.
# For the multiples of buzz print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

def fizz_buzz():
    numbers = [i for i in range(1, 101)]
    for num in numbers:
        if num % 3 == 0 and num % 5 != 0:
            print(f'{num}: fizz')
        elif num % 5 == 0 and num % 3 != 0:
            print(f'{num}: buzz')
        elif num % 15 == 0:
            print(f'{num}: fizzbuzz')
        else:
            print(f'{num}: {num}')
