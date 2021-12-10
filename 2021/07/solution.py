with open("input.txt", "r") as f:
    pos = [int(i) for i in f.read().strip().split(",")]


def triangle(n):
    return n * (n + 1) // 2


def eval_pos(pos, test):
    fuel = 0
    for i in pos:
        fuel += triangle(abs(test - i))
    return fuel


fuel = eval_pos(pos, max(pos) + 1)
for i in range(min(pos), max(pos)):
    fuel = min(fuel, eval_pos(pos, i))
print(fuel)
