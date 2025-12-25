import sys

def find_max_joltage(bank: list[int]) -> int:
    curr = 0
    index = 0
    for i in range(12):
        max_digit = -1
        argmax = -1
        end = len(bank) - 11 + i
        for j in range(index, end):
            if bank[j] > max_digit:
                max_digit = bank[j]
                argmax = j
        curr = curr * 10 + max_digit
        index = argmax + 1
    return curr

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return
    answer = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            bank = [int(c) for c in line.strip()]
            answer += find_max_joltage(bank)
    print(answer)

if __name__ == "__main__":
    main()
