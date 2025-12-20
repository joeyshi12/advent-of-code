import sys

def is_repeated_sequence(product_id: str, num_occurrances: int) -> int:
    sequence_size = len(product_id) // num_occurrances
    sequence = product_id[:sequence_size]
    for i in range(1, num_occurrances):
        if sequence != product_id[sequence_size * i:sequence_size * (i + 1)]:
            return False
    return True

def is_invalid_id(product_id: int) -> bool:
    id_str = str(product_id)
    for divisor in range(2, len(id_str) + 1):
        if len(id_str) % divisor != 0:
            continue
        if is_repeated_sequence(id_str, divisor):
            return True
    return False

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    answer = 0
    with open(sys.argv[1], "r") as f:
        id_ranges = f.read().strip().split(",")
        for id_range in id_ranges:
            start, end = [int(endpoint) for endpoint in id_range.split("-")]
            for i in range(start, end + 1):
                if is_invalid_id(i):
                    answer += i

    print(answer)

if __name__ == "__main__":
    main()
