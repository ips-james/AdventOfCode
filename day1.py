expense_list = [int(line) for line in open('day1_input.txt', 'r')]

for e in expense_list:
    for f in expense_list:
        if e + f > 2020:
            continue
        if e + f == 2020:
            print(e, f, e * f)

        for g in expense_list:
            if e + f + g > 2020:
                continue
            if e + f + g == 2020:
                print(e, f, g, e * f * g)
