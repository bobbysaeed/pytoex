"""
Write code that finds the numbers  between 7801 and 8853  that  sum of all their integers are divisible by 13.

"""
for num in range(7801, 8854):
    elements = [int(n) for n in str(num)]
    if sum(elements) % 13 == 0:
        print(num)
