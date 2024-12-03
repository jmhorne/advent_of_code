"""
Advent of Code 2024
Day 3
Author: James M. Horne
"""

import re

def mul(line):
    """
    parses a mul(*) command and returns the result

    line: mul command line

    returns result of mul command
    """
    l, r = [int(x) for x in re.findall(r"\d{1,3},\d{1,3}", line)[0].split(',')]
    return l * r

if __name__ == '__main__':
    with open(file='./puzzle_input/3', encoding='utf-8') as f:
        puzzle = f.read()

    print(f"Part 1: {sum((mul(x.group()) for x in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", puzzle)))}")

    ENABLED = True
    TOTAL = 0

    for p in re.finditer(r"mul\(\d{1,3},\d{1,3}\)|do(n't)?\(\)", puzzle):
        ins = p.group()

        if ins == "do()":
            ENABLED = True
            continue

        if ins == "don't()":
            ENABLED = False
            continue

        if ENABLED:
            TOTAL += mul(ins)

    print(f"Part 2: {TOTAL}")
