with open("input.txt", "r") as f:
    lines = [i.strip() for i in f]

OPENING = ("(", "[", "{", "<")
CLOSING = (")", "]", "}", ">")

def find_invalid(line):
    for i in range(len(line) - 1):
        try:
            index = OPENING.index(line[i])
            assert CLOSING[index] == line[i + 1]
        except AssertionError:
            pass
        except ValueError:
            pass
        else:
            line.pop(i)
            line.pop(i)

for item in lines:
    