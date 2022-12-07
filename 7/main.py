""" Solution to AOC 2022 - 7 """

import sys
from re import match
from pdb import set_trace


class ChildNotFound(Exception):
    pass


class Filesystem:
    def __init__(self):
        self.root = Folder("root", None)
        self.pos = self.root

    def add_folder(self, name):
        self.pos.add_folder(name, self.pos)

    def add_file(self, name, size):
        self.pos.add_file(name, size)

    def goto_root(self):
        self.pos = self.root

    def goto_folder(self, name):
        if name == ".." and self.pos.parent:
            self.pos = self.pos.parent
            return

        for folder in self.pos.folders:
            if folder.name == name:
                self.pos = folder
                return

        raise ChildNotFound(f"Folder '{name}' not found")

    def print(self):
        self.root.print()


class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.folders = []
        self.files = []
        self.size = None

    def add_folder(self, name, parent):
        self.folders.append(Folder(name, parent))

    def add_file(self, name, size):
        self.files.append(File(name, size))

    def get_depth(self):
        return self.parent.get_depth() + 1 if self.parent else 0

    def print(self):
        pad = 2 * self.get_depth()
        print(" " * pad + f"- {self.name} (dir, size={self.size})")
        for folder in self.folders:
            folder.print()
        for file in self.files:
            print(" " * (pad + 2) + f"- {file.name} (file, size={file.size})")


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def build_tree(commands):
    """Build the file tree from commands."""

    filesystem = Filesystem()

    while commands:
        command = commands.pop(0)

        # Check for a change of directory.
        cd_dir = match(r"\$ cd ([a-z\/.]+)", command)
        if cd_dir:
            if cd_dir.group(1) == "/":
                filesystem.goto_root()
            else:
                filesystem.goto_folder(cd_dir.group(1))
            continue

        if command == "$ ls":
            # Get all files and folders listed
            while commands and commands[0][0] != "$":
                command = commands.pop(0)

                if command.startswith("dir"):
                    filesystem.add_folder(command.split(" ")[1])
                else:
                    size, name = command.split(" ")
                    filesystem.add_file(name, int(size))

    return filesystem


def calc_folder_sizes(tree_pos):
    folder_sizes = []
    if tree_pos.folders:
        for folder in tree_pos.folders:
            folder_sizes.extend(calc_folder_sizes(folder))

    current_folder_size = sum([folder.size for folder in tree_pos.folders]) + sum(
        [file.size for file in tree_pos.files]
    )
    folder_sizes.append(current_folder_size)
    tree_pos.size = current_folder_size

    return folder_sizes


if __name__ == "__main__":
    file_in = sys.argv[1]

    with open(file_in, "r") as fh:
        commands = [line.strip("\n") for line in fh.readlines()]

    tree = build_tree(commands)
    folder_sizes = calc_folder_sizes(tree.root)
    tree.print()

    limit = 100000
    print(
        "[Task 1] Number of folders smaller than {} is {} with a sum of {}".format(
            limit,
            sum([1 for size in folder_sizes if size <= limit]),
            sum([size for size in folder_sizes if size <= limit]),
        )
    )

    total_size = 70000000
    req_size = 30000000
    to_delete = req_size - (total_size - max(folder_sizes))
    print(
        "[Task 2] Smallest directory to remove is of size {}".format(
            min(folder_sizes, key=lambda x: abs(x - to_delete))
        )
    )
