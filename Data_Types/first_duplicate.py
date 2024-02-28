#Given an array a that contains only numbers in the range from 1 to a.
# length, find the first duplicate number for which the second occurrence has the minimal index.
# In other words, if there are more than 1 duplicated number,
# print the number for which the second occurrence has a smaller index
# than the second occurrence of the other number does.
# If there are no such elements, print -1.



a = [2, 1, 3, 5, 3, 2]

new_a = []
for num in a:
    if num in new_a:
        print(num)
        break
    new_a.append(num)
else:
    print(-1)