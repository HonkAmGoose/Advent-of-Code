with open("input.txt", "r") as f:
    fish = [int(i) for i in f.read().strip("\n").split(",")]


fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for value in fish:
    fishes[value] += 1

for i in range(256):
    j = i % 6
    zero = fishes.pop(0)
    fishes[6] += zero
    fishes.append(zero)
    print(fishes)

total = 0
for i in fishes:
    total += i
print(total)
