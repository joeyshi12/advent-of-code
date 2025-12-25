import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    available_ingredients = 0
    with open(sys.argv[1], "r") as f:
        fresh_id_ranges = []

        for line in f:
            if line.isspace():
                break
            fresh_id_ranges.append([int(endpoint) for endpoint in line.split("-")])

        for line in f:
            ingredient_id = int(line)
            for start, end in fresh_id_ranges:
                if ingredient_id >= start and ingredient_id <= end:
                    available_ingredients += 1
                    break

    print(available_ingredients)

if __name__ == "__main__":
    main()
