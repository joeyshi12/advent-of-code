import sys

def is_accessible(row: int, col: int, roll_map: list[list[bool]]) -> bool:
    m, n = len(roll_map), len(roll_map[0])
    roll_count = 0
    for row_delta in range(-1, 2):
        for col_delta in range(-1, 2):
            if row_delta == 0 and col_delta == 0:
                continue
            curr_row = row + row_delta
            curr_col = col + col_delta
            if curr_row < 0 or curr_row >= m or curr_col < 0 or curr_col >= n:
                continue
            if roll_map[curr_row][curr_col]:
                roll_count += 1
    return roll_count < 4

def count_accessible(roll_map: list[list[bool]]) -> int:
    m, n = len(roll_map), len(roll_map[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if roll_map[i][j] and is_accessible(i, j, roll_map):
                count += 1
    return count

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    with open(sys.argv[1], "r") as f:
        grid = []
        for line in f:
            grid.append([char == "@" for char in line.strip()])
        print(count_accessible(grid))

if __name__ == "__main__":
    main()
