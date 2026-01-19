def path_count(filename: str) -> int:
    graph = {}
    with open(filename, "r") as f:
        for line in f:
            source, targets = line.split(": ")
            graph[source] = [target for target in targets.split()]

    count = 0
    stack = ["you"]
    while stack:
        u = stack.pop()
        if u == "out":
            count += 1
            continue
        for v in graph[u]:
            stack.append(v)

    return count


def main():
    test_cases = [
        "example.txt",
        "input.txt"
    ]
    for filename in test_cases:
        answer = path_count(filename)
        print(f"{filename}: {answer}")


if __name__ == "__main__":
    main()
