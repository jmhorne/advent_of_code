"""
Advent of Code 2015
Day 5
Author: James M. Horne
"""

from re import match

if __name__ == '__main__':
    with open(file='puzzle_input/5', encoding='utf-8') as f:
        puzzle = f.readlines()

    print(f"Part 1: {sum(bool(match(r"^(?=(?:[^aeiou]*[aeiou]){3})(?=.*(\w)\1)(?!.*(ab|cd|pq|xy)).*$", x)) for x in puzzle)}")
    print(f"Part 2: {sum(bool(match(r"^(?=.*(\w\w).*\1)(?=.*(\w).\2).*$", x)) for x in puzzle)}")
