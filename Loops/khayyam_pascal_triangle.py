"""
    Write code that produces the following output:

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1

"""
n = 5
for i in range(n):
    print(" " * (n-i), end="")
    for j in range(i+1):
        if j == 0 or j == i:
            output = 1
        else:
            output= int(output * (i-j+1) / j)
        print(output, end=" ")
    print()