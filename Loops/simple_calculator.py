# Create a simple calculator for additions!
# Repeatedly ask the user to enter numbers.
#  Each time that the user provides input, this input is first converted to float
#  and then added to a running total (which should start from 0).
#  When the user enters add, the loop stops, and the running total is printed out.


total = 0
while True:
    num = input('enter a random number(or add to quit): ')
    if num == 'add':
        break
    total += float(num)
print(total)