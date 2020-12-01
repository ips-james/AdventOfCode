expense_list = {int(line) for line in open('day1_input.txt', 'r')}

print(next(x * y for x in expense_list for y in expense_list if x + y == 2020))
print(next(x * y * z for x in expense_list for y in expense_list for z in expense_list if x + y + z == 2020))
