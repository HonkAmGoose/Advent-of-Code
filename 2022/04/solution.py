# between 341 and 682

with open("input.txt", "r") as file:
    lines = []
    for line in file.readlines():
        split = (line.strip().replace(",", "-").split("-"))
        for i in range(4):
            split[i] = int(split[i])
        lines.append(split)

print(lines)

total = 0
for line in lines:
    if (line[0] <= line[2] <= line[1]) or (line[0] <= line[3] <= line[1]) or (line[2] <= line[0] <= line[3]) or (line[2] <= line[1] <= line[3]):
        total += 1
        print(line)
print(total)