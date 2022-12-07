""" Solution to AOC 2022 - 6 """

import sys


def find_start_index(line, length=4):
    """Find the index of the first four unique characters."""

    candidate = length

    while candidate < len(line):
        if len(set(line[candidate - length : candidate])) == length:
            return candidate
        candidate += 1

    return None


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]

    for line in lines:
        start_index = find_start_index(line)
        print(f"[Task 1] Start index is: {start_index}")

    for line in lines:
        start_index = find_start_index(line, length=14)
        print(f"[Task 2] Start index is: {start_index}")
