import math

input_map = [line for line in open('day3_input.txt', 'r')]


def sledge(step_x, step_y):
    limit_x = len(input_map[0]) - 1
    limit_y = len(input_map)

    x = y = 0
    trees = 0

    # print(limit_x, limit_y)
    for n in range(round(limit_y / step_y)):
        # print(x, y)
        if input_map[y][x] == "#":
            trees += 1
        # print(input_map[y][x], x, y, trees)
        x += step_x
        y += step_y
        if x >= limit_x:
            x = x - limit_x
    return (trees)


test_cases = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

results = [sledge(*test) for test in test_cases]
print(results)
print(math.prod(results))
