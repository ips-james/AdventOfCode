import re
input_entry = [line for line in open('day2_input.txt', 'r')]

# input_entry = ['1-3 a: abcde',
#                '1-3 b: cdefg',
#                '2-9 c: ccccccccc']
count_valid = 0
for entry in input_entry:

    result = re.match(r"(\d+)-(\d+) (.): (.*)", entry)

    valid = False

    lower_bound = int(result.group(1))
    upper_bound = int(result.group(2))
    check_letter = result.group(3)
    password = result.group(4)

    # found = 0
    # for x in password:
    #     if x == check_letter:
    #         found += 1
    # if lower_bound <= found <= upper_bound:
    #     valid = True
    #     count_valid += 1

    # print(found, valid)
    list_to_check = [password[lower_bound - 1], password[upper_bound - 1]]
    if list_to_check.count(check_letter) == 1:
        count_valid += 1

print(count_valid)
