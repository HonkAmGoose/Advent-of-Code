with open("input.txt", "r") as f:
    lines = [i.strip().split(" | ") for i in f]
# print(lines)

total = 0
UNIQUES = (2, 4, 3, 7)
for i in lines:
    for j in i[1].split(" "):
        if len(j) in UNIQUES:
            total += 1
print(total)
