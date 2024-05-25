rows = 7
for i in range(rows):
    if i in [0, 3]:
        print('*' * 4)
        # print()
    elif i in [1, 2]:
        print('*   *')
    else:
        print('*' + ' ' * (i -3) + '*')