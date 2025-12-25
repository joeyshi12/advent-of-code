import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    password = 0
    dial = 50
    with open(sys.argv[1], "r") as f:
        for line in f:
            sign = 1 if line[0] == "R" else -1
            distance = int(line[1:])

            num_cycles = distance // 100
            remainder = distance % 100
            password += num_cycles

            if dial != 0 and ((sign < 0 and dial <= remainder) or (sign > 0 and dial + remainder >= 100)):
                password += 1

            dial = (dial + distance * sign) % 100

    print(password)

if __name__ == "__main__":
    main()
