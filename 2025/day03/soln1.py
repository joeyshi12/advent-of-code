import sys

def find_max_joltage(bank: str) -> int:
    max_first_digit = -1
    index = -1
    for i in range(len(bank) - 1):
        digit = int(bank[i])
        if digit > max_first_digit:
            max_first_digit = digit
            index = i

    max_second_digit = -1
    for i in range(index + 1, len(bank)):
        max_second_digit = max(max_second_digit, int(bank[i]))

    return max_first_digit * 10 + max_second_digit

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    answer = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            answer += find_max_joltage(line.strip())

    print(answer)

if __name__ == "__main__":
    main()
