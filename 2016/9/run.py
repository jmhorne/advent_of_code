#!/usr/bin/env python3

import re

class Puzzle:
    def __init__(self, input_filename):
        with open(input_filename, 'r') as f:
            self._raw = f.read()
        self._p1_len = 0
        self._p2_len = 0

    def _parse(self, chunk):
        pass

    def part1(self):
        chunk = list(self._raw)

        while len(chunk):
            break


    def part2(self):
        pass


if __name__ == '__main__':
    puzzle = Puzzle("test.txt")
    print(f"Part 1: {puzzle.part1()}")
    print(f"Part 2: {puzzle.part2()}")

# END OF FILE
