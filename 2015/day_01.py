"""
Advent of Code 2015
Day 1
Author: James M. Horne
"""

from collections import defaultdict

if __name__ == '__main__':
    dirs = defaultdict(int, {"(":1, ")":-1})

    with open(file='puzzle_input/1', encoding='utf-8') as f:
        puzzle = f.read()

    print(f"Part 1: {sum((dirs[x] for x in puzzle))}")

    FLOOR = 0
    COUNT = 0
    for char in puzzle:
        COUNT += 1
        FLOOR += dirs[char]
        if FLOOR < 0:
            break
    print(f"Part 2: {COUNT}")
