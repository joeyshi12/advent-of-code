import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    grid: list[list[str]] = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            grid.append(list(line.strip()))

    width = len(grid[0])
    beam_row = [int(c == "S") for c in grid[0]]
    for i in range(1, len(grid)):
        next_beam_row = [0] * width
        for j, cell in enumerate(beam_row):
            if not cell:
                continue
            if grid[i][j] == ".":
                next_beam_row[j] += beam_row[j]
                continue
            if j > 0:
                next_beam_row[j - 1] += beam_row[j]
            if j < width - 1:
                next_beam_row[j + 1] += beam_row[j]
        beam_row = next_beam_row

    print(sum(beam_row))

if __name__ == "__main__":
    main()
