with open("input.txt", "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(line.strip().replace("move ", "").replace(" from ", "*").replace(" to ", "*").split("*"))

for line in lines:
    for i in range(3):
        line[i] = int(line[i])

stacks = [[], ['B', 'Z', 'T'], ['V', 'H', 'T', 'D', 'N'], ['B', 'F', 'M', 'D'], ['T', 'J', 'G', 'W', 'V', 'Q', 'L'], ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'], ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'], ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'], ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'], ['M', 'Q', 'L', 'F', 'D', 'S']]

for line in lines:
    temp = []
    for i in range(line[0]):
        temp.append(stacks[line[1]].pop())
    for i in range(line[0]):
        stacks[line[2]].append(temp.pop())

print(stacks)