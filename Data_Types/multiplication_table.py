n = int(input('please choose a number: '))
for i in range(1, 11):
    print(f'{i:=2}  * {n:=2}    = {i * n:=3}')