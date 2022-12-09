""" Solution to AOC 2022 - 10 """

import sys

CYCLES_OF_INTEREST = [x for x in range(20, 221, 40)]
CRT_NEW_LINES = [x for x in range(40, 241, 40)]


def calc_signal_strength(instructions: list[tuple[str, str]]) -> int:
    """Calculate the signal strength from the instructions."""

    crt = [["." for _ in range(40)]]
    signal_strength = []
    register = 1
    cycle = 1

    for instruction in instructions:
        cycles = 1 if instruction[0] == "noop" else 2

        for _ in range(cycles):
            if cycle in CYCLES_OF_INTEREST:
                signal_strength.append(cycle * register)

            if cycle in CRT_NEW_LINES:
                crt.append(["." for _ in range(40)])

            if abs(((cycle - 1) % 40) - register) <= 1:
                crt[-1][(cycle - 1) % 40] = "#"
            cycle += 1

        if instruction[0] == "addx":
            register += int(instruction[1])

    return sum(signal_strength), crt


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        instructions = [line.strip().split(" ") for line in fh.readlines()]

    signal_strength, crt = calc_signal_strength(instructions)

    print(f"[Task 1] Sum of signal strengths is {signal_strength}")

    print("[Task 2]:")
    for line in crt:
        for row in line:
            print(row, end="")
        print()
