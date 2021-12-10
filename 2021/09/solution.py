with open("2021/09/input.txt", "r") as f:
    lines = [i.strip() for i in f]

risk = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i > 0 and j > 0 and i < len(lines) - 1 and j < len(lines[0]) - 1:
            test = int(lines[i][j])
            if test < min(
                int(lines[i + 1][j]),
                int(lines[i - 1][j]),
                int(lines[i][j + 1]),
                int(lines[i][j - 1]),
            ):
                risk += 1 + test
        elif i > 0 and j > 0 and i < len(lines) - 1:
            test = int(lines[i][j])
            if test < min(
                int(lines[i + 1][j]),
                int(lines[i - 1][j]),
                int(lines[i][j - 1]),
            ):
                risk += 1 + test
        elif i > 0 and j > 0 and j < len(lines[0]) - 1:
            test = int(lines[i][j])
            if test < min(
                int(lines[i - 1][j]),
                int(lines[i][j + 1]),
                int(lines[i][j - 1]),
            ):
                risk += 1 + test
        elif i > 0 and i < len(lines) - 1 and j < len(lines[0]) - 1:
            test = int(lines[i][j])
            if test < min(
                int(lines[i + 1][j]),
                int(lines[i - 1][j]),
                int(lines[i][j + 1]),
            ):
                risk += 1 + test
        elif j > 0 and i < len(lines) - 1 and j < len(lines[0]) - 1:
            test = int(lines[i][j])
            if test < min(
                int(lines[i + 1][j]),
                int(lines[i][j + 1]),
                int(lines[i][j - 1]),
            ):
                risk += 1 + test
risk += 4 + 2
print(risk)
