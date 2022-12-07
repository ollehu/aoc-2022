""" Solution to AOC 2022 - 5 """

import sys
from copy import deepcopy
from re import finditer, match


def get_column_indices(lines):
    """Get the indices for the columns of crates."""

    # The column row is the first line with only spaces and digits.
    for index, line in enumerate(lines):
        if match(r"^[ \d]+$", line):
            return index, [m.start(0) for m in finditer(r"\d", line)]
    raise Exception("Bad format")


def generate_crates(lines, row_index, columns):
    """Generate the crate columns ."""

    crates = [[] for _ in range(len(columns))]
    for row in range(0, row_index):
        for column_index, column in enumerate(columns):
            if lines[row][column] == " ":
                continue
            crates[column_index].append(lines[row][column])

    return crates


def print_crates(crates):
    """Help function to print the current status of crates."""

    crates = deepcopy(crates)
    print_str = [" " + "   ".join(map(str, range(len(crates))))]
    height = max([len(column) for column in crates])
    for _ in range(height):
        row_str = ""
        for column in range(len(crates)):
            if crates[column]:
                row_str += "[" + crates[column].pop() + "] "
            else:
                row_str += " " * 4
        print_str.append(row_str)

    for line in reversed(print_str):
        print(line)
    print("-" * max([len(line) for line in print_str]))


def generate_moves(lines):
    """Generate moves from lines."""

    search_str = r"move (\d+) from (\d+) to (\d+)"

    moves = []
    for line in lines:
        result = match(search_str, line)
        if result:
            # Moves are 1-indexed, decrement column indices
            moves.append((int(result.group(1)), int(result.group(2)) - 1, int(result.group(3)) - 1))

    return moves


def perform_move_9000(move, crates):
    """Execute a move on the crates (CrateMover9000)."""

    count = move[0]
    from_pile = move[1]
    to_pile = move[2]

    for _ in range(count):
        item = crates[from_pile].pop(0)
        crates[to_pile].insert(0, item)


def perform_move_9001(move, crates):
    """Execute a move on the crates (CrateMover9001)."""

    count = move[0]
    from_pile = move[1]
    to_pile = move[2]

    for index in range(count):
        item = crates[from_pile].pop(count - 1 - index)
        crates[to_pile].insert(0, item)


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        lines = [line.strip("\n") for line in fh.readlines()]

    row_index, columns = get_column_indices(lines)

    crates = generate_crates(lines, row_index, columns)
    moves = generate_moves(lines[row_index + 2 :])

    print_crates(crates)
    for move in moves:
        perform_move_9000(move, crates)
        print_crates(crates)

    print("[Task 1] Top crates are: {}".format("".join([col[0] for col in crates])))

    crates = generate_crates(lines, row_index, columns)

    print_crates(crates)
    for move in moves:
        perform_move_9001(move, crates)
        print_crates(crates)

    print("[Task 2] Top crates are: {}".format("".join([col[0] for col in crates])))
