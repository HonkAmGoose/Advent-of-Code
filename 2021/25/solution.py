## Move functions
def move(lines, moveSym, freeSym, x, y):
    xlen = len(lines[0])
    ylen = len(lines)
    for i in range(ylen):
        for j in range(xlen):
            if lines[i][j] == moveSym:
                if lines[(i + y) % ylen][(j + x) % xlen] == freeSym:
                    lines[(i + y) % ylen][(j + x) % xlen] = moveSym
                    lines[i][j] = freeSym
    return lines

def moveEast(lines):
    return move(lines, ">", ".", 1, 0)


def moveSouth(lines):
    return move(lines, "v", ".", 0, 1)

def nicePrint(lines):
    for i in lines:
        print("".join(i))
    print()

with open("test.txt", "r") as f:
    lines = []
    for i in f:
        lines.append([j for j in i.strip()])

nicePrint(lines)
previous = []
while previous != lines:
    previous = lines
    lines = moveEast(lines)
    nicePrint(lines)
    lines = moveSouth(lines)
    nicePrint(lines)
