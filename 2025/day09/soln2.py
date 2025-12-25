def max_area_with_red_tile_corners(input_file: str) -> int:
    red_tile_positions = read_red_tile_positions(input_file)
    max_area = -1
    size = len(red_tile_positions)
    for i in range(size - 1):
        for j in range(i + 1, size):
            x1, y1 = red_tile_positions[i]
            x2, y2 = red_tile_positions[j]
            if contains_non_corner_red_tile(x1, y1, x2, y2, red_tile_positions):
                continue
            width = abs(y1 - y2) + 1
            height = abs(x1 - x2) + 1
            max_area = max(max_area, width * height)

    return max_area


def contains_non_corner_red_tile(
    x1: int,
    y1: int,
    x2: int,
    y2: int,
    red_tile_positions: list[list[int]]
) -> bool:
    left, right = min(x1, x2), max(x1, x2)
    top, bottom = min(y1, y2), max(y1, y2)
    for i in range(1, len(red_tile_positions)):
        if not contains_point(red_tile_positions[i - 1], top, left, bottom, right):
            continue
        if not contains_point(red_tile_positions[i], top, left, bottom, right):
            continue
        if not contains_point(red_tile_positions[(i + 1) % len(red_tile_positions)], top, left, bottom, right):
            continue
        x, y = red_tile_positions[i]
        if (x == left or x == right) and (y == top or y == bottom):
            continue
        return True
    return False


def contains_point(position: list[int], top: int, left: int, bottom: int, right: int) -> bool:
    x, y = position
    return x >= left and x <= right and y >= top and y <= bottom


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
