import sys

def is_invalid_id(product_id: int) -> bool:
    id_str = str(product_id)
    if len(id_str) % 2 == 1:
        return False
    mid = len(id_str) // 2
    return id_str[:mid] == id_str[mid:]

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
