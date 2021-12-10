from sys import exit


with open("input.txt", "r") as f:
    lines = [i.strip().replace("  ", " ") for i in f]


def check_matrix(matrix):
    for i in range(5):
        if all((matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3], matrix[i][4])):
            return True
        if all((matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i], matrix[4][i])):
            return True
        return False  # If neither of the above return


# Get a list of integers representing the numbers called
# and a list of boards with the structure list[list[str(nn nn nn nn nn)]]
numbers = [int(i) for i in lines[0].split(",")]
boards = []
matrices = []
for i in range(len(lines) // 6):
    boards.append([])
    matrices.append([])
    for j in range(5):
        boards[i].append([])
        matrices[i].append([])
        for k in lines[6 * i + j + 2].split(" "):
            boards[i][j].append(int(k))
            matrices[i][j].append(False)


for num in numbers:
    for board_i, board in enumerate(boards):
        for line_i, line in enumerate(board):
            try:
                index = line.index(num)
            except ValueError:
                continue
            else:
                matrices[board_i][line_i][index] = True
        if check_matrix(matrices[board_i]):
            print("found")
            print(f"num {num}, board {board_i}, line {line_i}")
            print(f"board: {boards[board_i]}, matrix: {matrices[board_i]}")
            for i in board:
                print(i)
            for i in matrices[board_i]:
                print(i)
            exit()

# print(boards, numbers)
