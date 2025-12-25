from collections import deque


def min_presses(buttons: list[int], target: int) -> int:
    presses = 0
    queue = deque([0])
    visited = set([0])
    while queue:
        for _ in range(len(queue)):
            state = queue.popleft()
            if state == target:
                return presses
            for button in buttons:
                next_state = state ^ button
                if next_state in visited:
                    continue
                visited.add(next_state)
                queue.append(next_state)
        presses += 1
    return -1


def total_min_presses(filename: str) -> int:
    answer = 0
    with open(filename, "r") as f:
        for line in f:
            items = line.split()
            bit_str = "".join(reversed(["1" if c == "#" else "0" for c in items[0].strip("[]")]))
            target = int(bit_str, 2)
            buttons = []
            for i in range(1, len(items) - 1):
                button = 0
                for c in items[i].strip("()").split(","):
                    index = int(c)
                    button ^= 2 ** index
                buttons.append(button)
            answer += min_presses(buttons, target)
    return answer


def main():
    test_cases = ["example.txt", "input.txt"]
    for filename in test_cases:
        answer = total_min_presses(filename)
        print(f"{filename}: {answer}")


if __name__ == "__main__":
    main()
