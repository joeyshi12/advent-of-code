def max_area_with_red_tile_corners(input_file: str) -> int:
    red_tile_positions = read_red_tile_positions(input_file)
    max_area = -1
    size = len(red_tile_positions)
    for i in range(size - 1):
        for j in range(i + 1, size):
            x1, y1 = red_tile_positions[i]
            x2, y2 = red_tile_positions[j]
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            max_area = max(max_area, width * height)

    return max_area


def read_red_tile_positions(filename: str) -> list[list[int]]:
    red_tile_positions: list[list[int]] = []
    with open(filename, "r") as f:
        for line in f:
            red_tile_positions.append([int(num) for num in line.strip().split(",")])
    return red_tile_positions


def main():
    test_cases = ["example.txt", "input.txt"]
    for filename in test_cases:
        answer = max_area_with_red_tile_corners(filename)
        print(f"{filename}: {answer}")


if __name__ == "__main__":
    main()
