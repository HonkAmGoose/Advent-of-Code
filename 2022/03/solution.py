with open("input.txt", "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(line.strip())

chars = []
for i in range(len(lines) // 3):
    chars.append([
        item for item in lines[3*i] if item in lines[3*i + 1] and item in lines[3*i + 2]
    ])

total = 0
for chararr in chars:
    char = chararr[0]
    asc = ord(char)
    if 65 <= asc <= 90:
        asc -= 38
    elif 97 <= asc <= 122:
        asc -= 96
    total += asc

print(total)
