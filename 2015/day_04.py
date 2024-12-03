"""
Advent of Code 2015
Day 4
Author: James M. Horne
"""

from hashlib import md5

def find(puzzle:str, leading_zeros:int=5) -> int:
    """
    finds the first hex digest that has 'leading_zeros' amount of zeros

    puzzle: string to append numbers too
    leading_zeros: how many leading zeros should be in digest

    returns the number that when appended to puzzle produces desired digest
    """
    ans = 0

    while True:
        res = md5(f"{puzzle}{ans}".encode())

        if res.hexdigest()[:leading_zeros] == "0"*leading_zeros:
            break
        ans += 1
    return ans

if __name__ == '__main__':
    PUZZLE = "ckczppom"
    print(f"Part 1: {find(PUZZLE)}")
    print(f"Part 2: {find(PUZZLE, 6)}")
