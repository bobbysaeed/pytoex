# Write a program to print numbers from 1 to 40 except for multiples of 2 & 3.

for i in range(1, 41):
    if i % 2 == 0 or i % 3 == 0:
        continue
    else:
        print(i)