import array

current = 0
totals = []

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    for line in lines:
        if line == "":
            totals.append(current)
            current = 0
        else:
            current += int(line)

print(sorted(totals, reverse=True))
