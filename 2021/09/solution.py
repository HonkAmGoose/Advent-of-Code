with open("2021/09/input.txt", "r") as f:
    lines = [i.strip() for i in f]

basins = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != 9:
            pass

risk = 1
for i in basins:
    risk *= i
print(risk)
