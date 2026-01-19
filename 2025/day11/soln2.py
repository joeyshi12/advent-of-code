def read_graph(filename: str) -> dict[str, list[str]]:
    graph = {}
    with open(filename, "r") as f:
        for line in f:
            source, targets = line.split(": ")
            graph[source] = [target for target in targets.split()]
    return graph


def path_count(source: str,
               target: str,
               graph: dict[str, list[str]]) -> int:
    memo = {}
    def dfs(u: str) -> int:
        if u == target:
            return 1
        if u in memo:
            return memo[u]
        memo[u] = sum(dfs(v) for v in graph.get(u, []))
        return memo[u]
    return dfs(source)


def main():
    test_cases = [
        "example2.txt",
        "input.txt"
    ]
    for filename in test_cases:
        graph = read_graph(filename)
        answer = path_count("svr", "dac", graph) * path_count("dac", "fft", graph) * path_count("fft", "out", graph) \
            + path_count("svr", "fft", graph) * path_count("fft", "dac", graph) * path_count("dac", "out", graph)
        print(f"{filename}: {answer}")


if __name__ == "__main__":
    main()
