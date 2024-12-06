import copy

def rot_90(dir):
    if dir == [0, -1]:
        return [1, 0]
    elif dir == [1, 0]:
        return [0, 1]
    elif dir == [0, 1]:
        return [-1, 0]
    else:
        return [0, -1]

def has_loop(floor):
    floor2 = copy.deepcopy(floor)
    obstacle_positions = []
    gx, gy = 0, 0
    for y, line in enumerate(floor2):
        for x, char in enumerate(line):
            if char == "#":
                obstacle_positions += [[x, y]]
            elif char == "^":
                gx, gy = x, y

    path = []

    dr = [0, -1]
    while True:
        if dr[0] == 0:
            # Moving up or down
            if dr[1] == 1:
                # Moving down

                in_col = [obj for obj in obstacle_positions if obj[0] == gx]
                beneath = [obj for obj in in_col if obj[1] > gy]
                if not beneath:
                    return False
                nearest_beneath = list(sorted(beneath, key=lambda e: e[1]))[0]

                gy = nearest_beneath[1] - 1
                if [gx, gy, dr] in path:
                    return True
                
                path += [[gx, gy, dr]]
                dr = rot_90(dr)

            elif dr[1] == -1:
                # Moving up

                in_col = [obj for obj in obstacle_positions if obj[0] == gx]
                above = [obj for obj in in_col if obj[1] < gy]
                if not above:
                    return False
                nearest_above = list(sorted(above, key=lambda e: e[1], reverse=True))[0]

                gy = nearest_above[1] + 1
                if [gx, gy, dr] in path:
                    return True
                
                path += [[gx, gy, dr]]
                dr = rot_90(dr)

        else:
            if dr[0] == 1:
                in_row = [obj for obj in obstacle_positions if obj[1] == gy]
                right = [obj for obj in in_row if obj[0] > gx]
                if not right:
                    return False
                nearest_right = list(sorted(right, key=lambda e: e[0]))[0]

                gx = nearest_right[0] - 1
                if [gx, gy, dr] in path:
                    return True
                
                path += [[gx, gy, dr]]
                dr = rot_90(dr)

            elif dr[0] == -1:
                in_row = [obj for obj in obstacle_positions if obj[1] == gy]
                left = [obj for obj in in_row if obj[0] < gx]
                if not left:
                    return False
                nearest_left = list(sorted(left, key=lambda e: e[0], reverse=True))[0]

                gx = nearest_left[0] + 1
                if [gx, gy, dr] in path:
                    return True
                
                path += [[gx, gy, dr]]
                dr = rot_90(dr)

floor = list(map(list, open("input.txt", "r").read().split("\n")))
n = 0

for y, line in enumerate(floor):
    print(y)
    for x, char in enumerate(line):
        if char == ".":
            floor[y][x] = "#"
            if has_loop(floor):
                n += 1
            floor[y][x] = "."

print(n)
