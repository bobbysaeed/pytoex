# Write a program to print the following number pattern using a loop.

#   1 
#   1 2  
#   1 2 3  
#   1 2 3 4  
#   1 2 3 4 5

n = 2
while n <= 6:
    for i in range(1, n):
        print(i, '', end=' ')
    print()

    n += 1


# solution number 2:

# rows = 5
# numbers = []
# print(numbers)
# for i in range(1, rows+1):
#     numbers.append(i)
#     for num in numbers:
#         print(num, ' ', end='')
#     print()