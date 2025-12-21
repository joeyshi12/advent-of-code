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
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

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
    prev_joined_u = -1
    prev_joined_v = -1
    while edges:
        u, v, _ = edges.pop()
        if find(dsu, u) != find(dsu, v):
            prev_joined_u = u
            prev_joined_v = v
            union(dsu, u, v)

    print(positions[prev_joined_u][0] * positions[prev_joined_v][0])

if __name__ == "__main__":
    main()
