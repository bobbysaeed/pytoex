random_num_data = [
    18, 60, -10, 17, 55, 8, -1, 31, 52, 31,
    27, 14, 25, 0, -2, 15, -1, 50, 45, -4,
    42, -10, 40, 3, 43, 55, 24, -17, 17, 54,
    19, 24, 44, 30, 24, 3, -17, 31, 45, -10,
    13, -12, 21, -13, 52, 57, -1, 37, 21, 42
]

random_num_data.sort(reverse=True)

maximum = random_num_data[0]
minimum = random_num_data[-1]
print(f'the maximum is: {maximum} and the minimum number is: {minimum}')

sum_numbers = 0
for i in random_num_data:
    sum_numbers += i

print(f'total sum of numbers is: {sum_numbers}')

mean_numbers = sum_numbers / len(random_num_data)
print(f'the mean of these numbers is: {mean_numbers}')