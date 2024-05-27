# Write a Python program to check a string representing a number or not

numbers =[num for num in range(10)]
inp = str(input('enter your input: '))
for i in inp:
    if i in str(numbers):
        continue
    else:
        print("this is a string")
        break
else:
    print("all numbers")