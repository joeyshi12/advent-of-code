import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    lines = []
    operations = None
    with open(sys.argv[1], "r") as f:
        for line in f:
            if line.strip()[0].isdigit():
                lines.append(line)
            else:
                operations = line.split()

    if operations is None:
        return Exception("operations is None")

    matrix = []
    row = []
    for col in range(len(lines[0])):
        col_str = "".join(line[col] for line in lines)
        if col_str.isspace():
            matrix.append(row)
            row = []
        else:
            row.append(int(col_str))
    matrix.append(row)

    answer = 0
    for i, operation in enumerate(operations):
        if operation == "+":
            answer += sum(matrix[i])
        else:
            product = 1
            for num in matrix[i]:
                product *= num
            answer += product

    print(answer)

if __name__ == "__main__":
    main()
