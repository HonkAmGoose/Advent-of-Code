with open("input.txt", "r") as f:
    lines = f.readlines()

horiz = 0
depth = 0
angle = 0
for i in lines:
    com, num = i.strip().split()
    if com == "forward":
        horiz += int(num)
        depth += int(num) * angle
    elif com == "down":
        angle += int(num)
    elif com == "up":
        angle -= int(num)
    else:
        print("error")
print(horiz, depth, horiz*depth, sep = '\n')
