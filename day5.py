test = 'BBFFBBFRLL'
input_text = open('day5_input.txt', 'r').read().split("\n")
seat_id_max = 0

input_text.sort()


check_list = []
for line in input_text:

    # print (line[:7], line[7:])
    binary_row = ('').join(['0' if x == 'F' else '1' for x in line[:7]])
    binary_col = ('').join(['0' if x == 'L' else '1' for x in line[7:]])
    row = int(binary_row, 2)
    col = int(binary_col, 2)
    seat_id = (row * 8) + col
    if seat_id > seat_id_max:
        seat_id_max = seat_id
    check_list.append(seat_id)

    # print (line[:7], line[7:], binary_row, row, binary_col, col, seat_id)
print(seat_id_max)

for x in range(80, 920):
    if x not in check_list:
        print(x)
