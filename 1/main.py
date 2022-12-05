""" Solution to AOC 2022 - 1 """

import sys
from itertools import groupby

if __name__ == "__main__":
    file_in = sys.argv[1]

    calories = []
    with open(file_in, "r") as fh:
        lines = [line.strip() for line in fh.readlines()]

    calories = [list(map(int, x)) for i, x in groupby(lines, key=lambda x: x != "") if i]

    sum_of_calories = [sum(x) for x in calories]

    print("[Task 1] Top calories: {}".format(max(sum_of_calories)))

    sum_of_calories.sort()

    print("[Task 2] Sum of top three calories: {}".format(sum(sum_of_calories[-3:])))
