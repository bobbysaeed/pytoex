num = int(input("enter a number: "))
list_of_divisors = []
for i in range(1, num):
    if num % i == 0:
        list_of_divisors.append(i)
if num == sum(list_of_divisors):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")