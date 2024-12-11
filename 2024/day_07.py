"""
Advent of Code 2024
Day 7
Author: James M. Horne
"""

from itertools import product

def add(l, r):
    """
    returns l + r
    """
    return l + r

def mul(l, r):
    """
    return l * r
    """
    return l * r

def cat(l, r):
    """
    return l concantenatd with r
    """
    return int(f"{l}{r}")

def test_equation(equation, is_part2=False):
    """
    Tests whether an equation can be solved by manipulating possible operators

    returns value if true, returns 0 if false
    """
    if is_part2:
        possible_operators = list(product([add, mul, cat], repeat=len(equation[1]) - 1))
    else:
        possible_operators = list(product([add, mul], repeat=len(equation[1]) - 1))

    total = 0
    for po in possible_operators:
        total = equation[1][0]

        for i, o in enumerate(po):
            total = o(total, equation[1][i+1])

        if total == equation[0]:
            return total

    return 0

if __name__ == '__main__':
    with open('puzzle_input/7', encoding='utf-8') as f:
        puzzle = [[int(y[0]), [int(z) for z in y[1].split(' ')]] for y in [x.strip().split(': ') for x in f.readlines()]]

    print(f"Part 1: {sum((test_equation(p) for p in puzzle))}")
    print(f"Part 2: {sum((test_equation(p, True) for p in puzzle))}")
