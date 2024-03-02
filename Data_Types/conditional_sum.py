# num_1 = float(input("first grade: "))
# num_2 = float(input("second grade: "))
# num_3 = float(input("third grade: "))

# sum_of_nums = num_1 + num_2 + num_3
# mean_of_numbers = sum_of_nums / 3
# if mean_of_numbers in range(16, 21):
#     print("the final score is 20")
# else:
#     print(f"the final scorre is {mean_of_numbers}")


num_1 = float(input("first grade: "))
num_2 = float(input("second grade: "))
num_3 = float(input("third grade: "))

sum_of_nums = num_1 + num_2 + num_3
mean_of_numbers = sum_of_nums / 3
if mean_of_numbers >= 16:
    print("the final score is 20")
else:
    print(f"the final score is {mean_of_numbers}")