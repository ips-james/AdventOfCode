import math

input_map = open('day3_input.txt', 'r').read().splitlines()
# print(input_map)


def sledge(dx, dy):
    limit_x = len(input_map[0])
    limit_y = len(input_map)

    (x, y) = (0, 0)
    trees = 0

    # print(limit_x, limit_y)
    while y < limit_y:

        if input_map[y][x] == "#":
            trees += 1
        # print(x, y, trees)
        x = (x + dx) % limit_x
        y += dy
        # if x >= limit_x:
        #     x = x - limit_x
    return (trees)


test_cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

results = [sledge(*test) for test in test_cases]
print(results)
print(math.prod(results))
