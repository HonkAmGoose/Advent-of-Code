with open("input.txt", "r") as f:
    lines = [i.strip() for i in f]


def count_at_pos(in_list, pos):
    zeroes = 0
    ones = 1

    for i in in_list:
        if i[pos] == "0":
            zeroes += 1
        elif i[pos] == "1":
            ones += 1
        else:
            raise Exception("Help")

    return (zeroes, ones)


def remove_values(in_list, pos, val):
    out_list = []

    for i in in_list:
        if int(i[pos]) != val:
            out_list.append(i)

    return out_list


lines_o = list(lines)
for i in range(12):
    zeroes, ones = count_at_pos(lines_o, i)
    print(i, zeroes, ones)
    if zeroes < ones:
        lines_o = remove_values(lines_o, i, 0)
    else:
        lines_o = remove_values(lines_o, i, 1)
    print(lines_o, len(lines_o))
    if len(lines_o) == 1:
        break


lines_c = list(lines)
for i in range(12):
    zeroes, ones = count_at_pos(lines_c, i)
    print(i, zeroes, ones)
    if zeroes < ones:
        lines_c = remove_values(lines_c, i, 1)
    else:
        lines_c = remove_values(lines_c, i, 0)
    print(lines_c, len(lines_c))
    if len(lines_c) == 1:
        break


print(lines_o, lines_c)

print(int(lines_o[0], 2), int(lines_c[0], 2))


print("hi")
