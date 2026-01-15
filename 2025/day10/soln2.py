import scipy.optimize
import numpy as np


def min_presses(machine_config: str) -> int:
    items = machine_config.split()
    b_eq = np.array([int(c) for c in items[-1].strip("{}").split(",")])
    A_eq = np.zeros((b_eq.size, len(items) - 2))
    for j, button in enumerate(items[1:len(items) - 1]):
        for c in button.strip("()").split(","):
            i = int(c)
            A_eq[i, j] = 1

    c = np.ones(A_eq.shape[1])
    result = scipy.optimize.linprog(c, A_eq=A_eq, b_eq=b_eq, integrality=1)
    assert all(result.x >= 0)

    return int(np.sum(result.x))


def total_min_presses(filename: str) -> int:
    answer = 0
    with open(filename, "r") as f:
        for machine_config in f:
            answer += min_presses(machine_config)
    return answer


def main():
    test_cases = ["example.txt", "input.txt"]
    for filename in test_cases:
        answer = total_min_presses(filename)
        print(f"{filename}: {answer}")


if __name__ == "__main__":
    main()
