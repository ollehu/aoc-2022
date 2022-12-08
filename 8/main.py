""" Solution to AOC 2022 - 8 """

import sys
import numpy as np


def calc_trees_shown(trees):
    """Calculate the number of trees shown from each side."""

    height, width = trees.shape

    scenics = []
    trees_found = []

    for row in range(1, height - 1):
        for column in range(1, width - 1):
            if ((row, column) not in trees_found) and (
                all(trees[row, range(column)] < trees[row, column])
                or all(trees[row, range(column + 1, width)] < trees[row, column])
                or all(trees[range(row), column] < trees[row, column])
                or all(trees[range(row + 1, height), column] < trees[row, column])
            ):
                trees_found.append((row, column))

            scenic = 1

            directions = map(
                list,
                [
                    reversed(trees[row, range(column)]),
                    trees[row, range(column + 1, width)],
                    reversed(trees[range(row), column]),
                    trees[range(row + 1, height), column],
                ],
            )
            for direction in directions:
                try:
                    scenic *= [
                        idx for idx, val in enumerate(direction) if val >= trees[row, column]
                    ][0] + 1
                except IndexError:
                    # Is the largest tree in that direction.
                    scenic *= len(direction)
            scenics.append(scenic)

    return scenics, len(trees_found) + (height + width) * 2 - 4


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        trees = np.array([[int(x) for x in line.strip()] for line in fh.readlines()])

    scenics, trees_shown = calc_trees_shown(trees)

    print(f"[Task 1] Number of visible trees is {trees_shown}")
    print(f"[Task 2] Best scenic score is {max(scenics)}")
