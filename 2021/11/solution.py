with open("11/test.txt", "r") as f:
    lines = []
    for i in f:
        lines.append([int(j) for j in i.strip()])

flashes = 0


def increase(i, j):
    global lines, flashes
    lines[i][j] += 1
    if lines[i][j] > 9:
        flashes += 1
        lines[i][j] = -100
        if i > 0:
            increase(i - 1, j)
        if j > 0:
            increase(i, j - 1)
        if i < len(lines) - 1:
            increase(i + 1, j)
        if j < len(lines[0]) - 1:
            increase(i, j + 1)


I = len(lines)
J = len(lines[0])

for h in range(2):
    for i in range(I):
        for j in range(J):
            increase(i, j)

    print()

print(flashes)
