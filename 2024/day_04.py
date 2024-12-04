"""
Advent of Code 2024
Day 4
Author: James M. Horne
"""

import re
import numpy as np

with open(file='puzzle_input/4', encoding='utf-8') as f:
    puzzle = np.array([list(x.strip()) for x in f.readlines()])

rows, cols = puzzle.shape

# Part 1
#   check horizontals
total = sum(len(re.findall(r"(?=(XMAS|SAMX))", ''.join(p))) for p in puzzle)
#   check verticals
total += sum(len(re.findall(r"(?=(XMAS|SAMX))", ''.join(p))) for p in np.rot90(puzzle))
#   check diagonals
total += sum(len(re.findall(r"(?=(XMAS|SAMX))", ''.join(d))) for d in [np.diagonal(puzzle, offset=x) for x in range(-rows + 1, cols)] + [np.diagonal(np.fliplr(puzzle), offset=x) for x in range(-rows + 1, cols)])
print(f"Part 1: {total}")

# Part 2
total = sum(len(re.findall(r"M.S.A.M.S|S.M.A.S.M|S.S.A.M.M|M.M.A.S.S", ''.join(puzzle[row:row + 3, col:col + 3].flatten()))) for row in range(rows) for col in range(cols))
print(f"Part 2: {total}")
