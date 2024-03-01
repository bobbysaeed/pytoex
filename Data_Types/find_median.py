# Write a Python program to get 3 inputs from the user
# and find the median of three values without sorting values.
# only use conditional statements, not any python methods.

first_num = int(input("choose the first number: "))
second_num = int(input("choose the second number: "))
third_num = int(input("choose the third number: "))

if first_num > second_num:
    if second_num > third_num:
        print(f"the median is {second_num}")
    elif third_num > first_num:
        print(f"the median is {first_num}")
    else:
        print(f"the median is {third_num}")
else:
    if first_num > third_num:
        print(f"the median is {first_num}")
    elif second_num < third_num:
        print(f"the median is {second_num}")
    else:
        print(f"the median is {third_num}")