lines, maxx, maxy = [], 0, 0
with open("input.txt", "r") as f:
    for i in f:
        c1, c2 = i.strip().split(" -> ")
        x1, y1 = c1.split(",")
        x2, y2 = c2.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 == x2 or y1 == y2:
            lines.append([x1, y1, x2, y2])
        maxx = max(maxx, x1, x2)
        maxy = max(maxy, y1, y2)

grid = []
for i in range(maxx):
    grid.append([])
    for j in range(maxy):
        grid[i].append(0)

for i in lines:
    if i[0] == i[2]:
        if i[3] < i[1]:
            i[1], i[3] = i[3], i[1]
        for j in range(i[1], i[3] + 1):
            grid[i[0]][j] += 1
    if i[1] == i[3]:
        if i[2] < i[0]:
            i[0], i[2] = i[2], i[0]
        for j in range(i[0], i[2] + 1):
            grid[j][i[1]] += 1

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] >= 2:
            total += 1
print(total)
