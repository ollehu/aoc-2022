""" Solution to AOC 2022 - 11 """

import sys
import re

from math import floor, prod


class Monkey:
    def __init__(self, i: int) -> None:
        self.i = i
        self.items = []
        self.mod = None
        self.test = None
        self.buddies = [None, None]
        self.inspections = 0

    def set_data(self, items: list[int], op: str, mod: int, buddies: list["Monkey"]) -> None:
        self.items = list(items)
        self.op = op
        self.mod = mod
        self.buddies = buddies

    def play(self, monkeys: list["Monkey"], moduli: int, division: bool) -> None:
        while self.items:
            self.inspections += 1

            old = self.items.pop(0)
            new = eval(self.op)
            if division:
                new = floor(new / 3)
            new = new % moduli

            if new % self.mod == 0:
                monkeys[self.buddies[0]].items.append(new)
            else:
                monkeys[self.buddies[1]].items.append(new)

    def __str__(self):
        string = f"Monkey {self.i}\n"
        string += f"  Starting items:  {', '.join(map(str, self.items))}\n"
        string += f"  Operation: new = {self.op}\n"
        string += f"  Test: {self.test}\n"
        string += f"    If true: throw to monkey {self.buddies[0]}\n"
        string += f"    If false: throw to monkey {self.buddies[1]}\n"
        return string


def play_game(monkeys: list["Monkey"], division: bool = True, rounds: int = 20) -> list[int]:
    """Play the game and return each monkeys inspection count."""

    moduli = prod([monkey.mod for monkey in monkeys])

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.play(monkeys, moduli, division)

    return [monkey.inspections for monkey in monkeys]


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        line = fh.read()

    no_monkeys = len(re.findall(r"Monkey \d:", line))

    # Initiate empty monkeys, this is done to connect them later on.
    monkeys = [Monkey(i) for i in range(no_monkeys)]
    lines = [line.strip() for line in line.split("\n")]

    i = 0
    while lines:
        if "Monkey" in lines.pop(0):
            items = map(int, re.search(r": ([\d, ]+)", lines.pop(0)).group(1).split(","))
            op = re.search(r"new = (.+)", lines.pop(0)).group(1)
            mod = int(re.search(r"divisible by (\d+)", lines.pop(0)).group(1))
            true_buddy = int(re.search(r"monkey (\d+)", lines.pop(0)).group(1))
            false_buddy = int(re.search(r"monkey (\d+)", lines.pop(0)).group(1))

            monkeys[i].set_data(items, op, mod, [true_buddy, false_buddy])
            i += 1

    inspection_count = sorted(play_game(monkeys))
    print(inspection_count)
    print(f"[Task 1] Monkey business is {inspection_count[-1] * inspection_count[-2]}")

    inspection_count = sorted(play_game(monkeys, False, 10000))
    print(inspection_count)
    print(f"[Task 2] Monkey business is {inspection_count[-1] * inspection_count[-2]}")
