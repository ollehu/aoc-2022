""" Solution to AOC 2022 - 3 """

import sys

ORD_LOWER_CASE_A = 96  # a-z are worth 1-26
ORD_UPPER_CASE_A = 64 - 26  # A-Z are worth 27-52


def find_common_items(line):
    """Find the common items in line."""

    middle = len(line) // 2

    first_compartment = line[:middle]
    second_compartment = line[middle:]

    return set(first_compartment).intersection(second_compartment)


def get_priority(items):
    """Get the total priority for all items."""

    priority = 0
    for item in items:
        if item.isupper():
            priority += ord(item) - ORD_UPPER_CASE_A
        else:
            priority += ord(item) - ORD_LOWER_CASE_A

    return priority


def split_into_chunks(in_list, chunk_size):
    """Split a list into smaller chunks."""

    for i in range(0, len(in_list), chunk_size):
        yield in_list[i : i + chunk_size]


def find_badge(chunk):
    """Find the common badge in chunk (three lines)."""

    common_character = chunk[0]
    for line in chunk[1:]:
        common_character = set(common_character).intersection(line)

    return common_character


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        lines = [line.strip() for line in fh.readlines()]

    priority = 0
    for line in lines:
        common_items = find_common_items(line)
        priority += get_priority(common_items)

    print(f"[Task 1] Total priority is {priority}")

    priority = 0
    for chunk in split_into_chunks(lines, 3):
        badge = find_badge(chunk)
        priority += get_priority(badge)

    print(f"[Task 2] Total priority is {priority}")
