def robot_moves(moves):
    vrt_movement = 0
    hrz_movement = 0
    for move in moves:
        direction, amount = move.split()
        amount = int(amount)
        if direction.upper() == 'UP':
            vrt_movement += amount
        elif direction.upper() == 'DOWN':
            vrt_movement -= amount
        elif direction.upper() == 'RIGHT':
            hrz_movement += amount
        elif direction.upper() == 'LEFT':
            hrz_movement -= amount
    dist_value = ((hrz_movement ** 2) + (vrt_movement ** 2)) ** 0.5
    currnet_loc = (hrz_movement, vrt_movement)

    print(f'the distance robot came is {dist_value} and current location is {currnet_loc}')

moves = []
while True:
    dir_distance = input("enter a direction and steps(or 'end' to quit) :")
    if dir_distance.lower() == "end":
        break
    moves.append(dir_distance)
robot_moves(moves)