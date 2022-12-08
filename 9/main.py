""" Solution to AOC 2022 - 9 """

import sys
from itertools import accumulate
import numpy as np


class Board:
    def __init__(self, moves: list[tuple[str, int]], nodes: list["Node"]) -> None:
        """Define a board and calculate the required width and height."""
        self.nodes = nodes
        self.x_max = 1
        self.x_min = 0
        self.y_max = 1
        self.y_min = 0

        x = 1
        y = 1
        for move in moves:
            if move[0] == "U":
                y += move[1]
                self.y_max = max(self.y_max, y)
            elif move[0] == "D":
                y -= move[1]
                self.y_min = min(self.y_min, y)
            elif move[0] == "R":
                x += move[1]
                self.x_max = max(self.x_max, x)
            else:
                x -= move[1]
                self.x_min = min(self.x_min, x)

        # Zero-indexed
        self.y_max += 1
        self.x_max += 1
        self.y_min -= 1
        self.x_min -= 1

    def __str__(self) -> None:
        """Print the board."""

        board = ""
        for y in reversed(range(self.y_min, self.y_max)):
            for x in range(self.x_min, self.x_max):
                marker = "."
                for node in self.nodes:
                    if all(node.pos == (x, y)):
                        marker = node.marker
                board += marker
            board += "\n"

        return board


class Node:
    def __init__(self, marker: str, x: int = 0, y: int = 0) -> None:
        """Initiate a node."""
        self.marker = marker
        self.pos = np.array((x, y))
        self.history = [(x, y)]

    def is_adjacent_to(self, node: "Node") -> bool:
        """Check if nodes are adjacent."""
        return max(abs(self.pos - node.pos)) <= 1

    def move(self, vector: tuple[int, int]) -> None:
        """Make a move of length 1 in the given direction."""

        self.pos += vector
        self.history.append(tuple(self.pos))

    def __str__(self):
        """String representation."""

        return f"[{self.marker}] ({self.pos[0]}, {self.pos[1]})"


def calc_tail_visits(moves: list[tuple[str, int]], knots: int) -> list[tuple[int, int]]:
    """Calculate the positions of the tail given head moves."""

    vectors = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    rope = [Node("H")] + [Node(str(i)) for i in range(1, knots)]

    board = Board(moves, rope)

    for move in moves:
        for _ in range(move[1]):
            rope[0].move(vectors[move[0]])

            # Move remaining knots
            for prev_knot, knot in zip(rope, rope[1:]):
                if not knot.is_adjacent_to(prev_knot):
                    knot.move(np.clip(prev_knot.pos - knot.pos, -1, 1))

    return len(set(rope[-1].history))


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        moves = [
            (line.strip().split(" ")[0], int(line.strip().split(" ")[1])) for line in fh.readlines()
        ]

    tail_visits = calc_tail_visits(moves, knots=2)
    print(f"[Task 1] The tail has visited {tail_visits} spots")

    tail_visits = calc_tail_visits(moves, knots=10)
    print(f"[Task 2] The tail has visited {tail_visits} spots")
