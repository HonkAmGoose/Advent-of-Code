with open("input.txt", "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(line.strip().split(" "))

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

WIN = "Z"
DRAW = "Y"
LOSE = "X"

total = 0
for i in lines:
    if i[0] in ROCK:
        if i[1] in DRAW: # draw 3, rock 1
            total += 4
        elif i[1] in WIN: # win 6, paper 2
            total += 8
        elif i[1] in LOSE: # loss 0, scissors 3
            total += 3
    elif i[0] in PAPER:
        if i[1] in LOSE: # loss 0, rock 1
            total += 1
        elif i[1] in DRAW: # draw 3, paper 2
            total += 5
        elif i[1] in WIN: # win 6, scissors 3
            total += 9
    elif i[0] in SCISSORS:
        if i[1] in WIN: # win 6, rock 1
            total += 7
        elif i[1] in LOSE: # loss 0, paper 2
            total += 2
        elif i[1] in DRAW: # draw 3, scissors 3
            total += 6

print(total)

# 15013 is too high