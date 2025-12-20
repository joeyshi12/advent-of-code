import sys


"""
Notes:

Input: [[3, 5], [10, 14], [16, 20], [2, 18], [30, 31]]

Sort by lower bound: [2, 18], [3, 5], [10, 14], [16, 20], [30, 31]

Merge: [2, 20], [30, 31]

Count: 19 + 2 = 21
"""

def count_fresh_ids(intervals: list[list[int]]) -> int:
    count = 0

    intervals.sort(key=lambda interval: interval[0])
    curr_interval = intervals[0]
    for i in range(1, len(intervals)):
        start, end = intervals[i]
        if curr_interval[1] < start:
            count += get_interval_size(curr_interval)
            curr_interval = intervals[i]
        else:
            curr_interval[1] = max(curr_interval[1], end)

    count += get_interval_size(curr_interval)
    return count

def get_interval_size(interval: list[int]) -> int:
    return interval[1] - interval[0] + 1

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        return

    intervals = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            if line.isspace():
                break
            intervals.append([int(endpoint) for endpoint in line.split("-")])

    print(count_fresh_ids(intervals))

if __name__ == "__main__":
    main()
