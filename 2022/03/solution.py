with open("input.txt", "r") as file:
    lines = []
    for line in file.readlines():
        line = line.strip()
        mid = len(line)//2
        lines.append([line[:mid], line[mid:]])

chars = []
for line in lines:
    chars.append([item for item in line[0] if item in line[1]])

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