import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    grid: list[list[str]] = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    split_count = 0
    width = len(grid[0])
    beam_row = [c == "S" for c in grid[0]]
    for i in range(1, len(grid)):
        next_beam_row = [False] * width
        for j, cell in enumerate(beam_row):
            if not cell:
                continue
            if grid[i][j] == ".":
                next_beam_row[j] = True
                continue
            split_count += 1
            if j > 0:
                next_beam_row[j - 1] = True
            if j < width - 1:
                next_beam_row[j + 1] = True
        beam_row = next_beam_row

    print(split_count)

if __name__ == "__main__":
    main()
