""" Solution to AOC 2022 - 4 """

import sys


def read_pair(line):
    """Convert string on the format "x-y,z-w" to lower and upper limits."""

    line = line.split(",")
    pair_0 = list(map(int, line[0].split("-")))
    pair_1 = list(map(int, line[1].split("-")))

    return (pair_0[0], pair_1[0]), (pair_0[1], pair_1[1])


def is_full_overlap(lower, upper):
    """Find if there is a full overlap. In that case, return 1 else 0."""

    if (lower[0] >= lower[1] and upper[0] <= upper[1]) or (
        lower[0] <= lower[1] and upper[0] >= upper[1]
    ):
        return 1
    return 0


def is_overlap(lower, upper):
    """Find if there is any overlap. In that case, return 1 else 0."""

    if (upper[0] >= lower[1] and lower[0] <= upper[1]) or (
        lower[0] <= upper[1] and upper[0] >= lower[1]
    ):
        return 1
    return 0


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        lines = [line.strip() for line in fh.readlines()]

    overlaps = 0
    full_overlaps = 0
    for line in lines:
        lower, upper = read_pair(line)
        overlaps += is_overlap(lower, upper)
        full_overlaps += is_full_overlap(lower, upper)

    print(f"[Task 1] Number of complete overlaps is {full_overlaps}")
    print(f"[Task 2] Number of overlaps is {overlaps}")
