import sys
import heapq

def find(dsu: list[int], key: int):
    if dsu[key] == -1:
        return key
    dsu[key] = find(dsu, dsu[key])
    return dsu[key]

def union(dsu: list[int], key1: int, key2: int):
    root1 = find(dsu, key1)
    root2 = find(dsu, key2)
    if root1 == root2:
        return
    dsu[root1] = root2

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <num_joins>")
        return

    num_joins = int(sys.argv[2])
    positions = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            positions.append([int(num) for num in line.strip().split(",")])

    edges = []
    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            p, q = positions[i], positions[j]
            weight = sum((p[i] - q[i]) ** 2 for i in range(3))
            edges.append([i, j, weight])

    edges.sort(key=lambda edge: edge[2], reverse=True)
    dsu = [-1] * len(positions)
    for _ in range(num_joins):
        u, v, _ = edges.pop()
        union(dsu, u, v)

    component_sizes = {}
    for i, _ in enumerate(dsu):
        rep = find(dsu, i)
        component_sizes[rep] = component_sizes.get(rep, 0) + 1

    top_sizes = []
    for size in component_sizes.values():
        heapq.heappush(top_sizes, size)
        if len(top_sizes) > 3:
            heapq.heappop(top_sizes)

    answer = 1
    for size in top_sizes:
        answer *= size

    print(answer)

if __name__ == "__main__":
    main()
