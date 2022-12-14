""" Solution to AOC 2022 - 13 """

import sys
from functools import cmp_to_key
from itertools import chain

from pdb import set_trace


def compare(left, right):
    for i in range(len(max(left, right, key=lambda x: len(x)))):
        try:
            left_ = left[i]
        except IndexError:
            return -1
        try:
            right_ = right[i]
        except IndexError:
            return 1

        # Assume equal
        equal = 0
        if type(left_) == type(right_) == int:
            if left_ < right_:
                equal = -1
            elif left_ > right_:
                equal = 1
        elif type(left_) == type(right_) == list:
            equal = compare(left_, right_)
        else:
            left_ = [left_] if isinstance(left_, int) and isinstance(right_, list) else left_
            right_ = [right_] if isinstance(left_, list) and isinstance(right_, int) else right_
            equal = compare(left_, right_)
        if equal:
            return equal
    return 0


def cound_sorted(pairs) -> int:
    """Return the indices of pairs sorted in the correct order."""

    i = 1
    i_sorted = []
    for left, right in pairs:
        if compare(left, right) == -1:
            i_sorted += [i]
        i += 1

    return i_sorted


def sort_packages(pairs):
    """Sort the packages including [[2]] [[6]]."""

    return sorted(list(chain(*pairs)) + [[[2]]] + [[[6]]], key=cmp_to_key(compare))


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        lines = [line.strip() for line in fh.readlines() if line.strip()]

    pairs = []
    for line_1, line_2 in zip(lines[::2], lines[1::2]):
        pairs.append((eval(line_1), eval(line_2)))

    i_sorted = cound_sorted(pairs)

    print(f"Sum of sorted is {sum(i_sorted)}")

    sort = sort_packages(pairs)

    print(f"[Task 2] Product of indices is {(sort.index([[2]]) + 1) * (sort.index([[6]]) + 1)}")
