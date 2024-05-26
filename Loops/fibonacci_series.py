n = 10
fibo = []

[fibo.append(fibo[-1] + fibo[-2]) if i >= 2 else fibo.append(i) for i in range(n)]

print(fibo)
