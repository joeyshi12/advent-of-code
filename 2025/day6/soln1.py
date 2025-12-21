import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    matrix = []
    operations = None
    with open(sys.argv[1], "r") as f:
        for line in f:
            row = line.split()
            if row[0].isnumeric():
                matrix.append([int(num) for num in row])
            else:
                operations = row

    if operations is None:
        raise Exception("Operations is None")

    answer = 0
    m, n = len(matrix), len(matrix[0])
    for col in range(n):
        if operations[col] == "+":
            answer += sum(matrix[row][col] for row in range(m))
        else:
            product = 1
            for row in range(m):
                product *= matrix[row][col]
            answer += product

    print(answer)

if __name__ == "__main__":
    main()
