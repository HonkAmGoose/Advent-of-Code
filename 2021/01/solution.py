with open("1_input.txt", "r") as f:
    lines = f.readlines()

totals = []
for i in range(len(lines) - 2):
    total = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    totals.append(total)

number = 0
for i in range(len(totals) - 1):
    if totals[i] < totals[i+1]:
        number += 1
        print(number)
