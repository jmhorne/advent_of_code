#!/usr/bin/env python3

import re

class Puzzle:
    def __init__(self, input_filename):
        self._fn = input_filename

    def _parse_chunk(self, chunk):
        dims = ""
        amount_read = len(chunk)
        chunk = chunk[1:]
        while chunk[0] != ')':
            dims += chunk[0]
            chunk = chunk[1:]
        chunk = chunk[1:]

        return [int(x) for x in dims.split('x')], amount_read - len(chunk)

    def _parse_compression(self):
        dims = ""

        self._data = self._data[1:]
        while self._data[0] != ')':
            dims += self._data[0]
            self._data = self._data[1:]
        self._data = self._data[1:]

        dims = [int(x) for x in dims.split('x')]
        return dims

    def _parse(self):
        if self._data[0] == '(':
            dims = self._parse_compression()
            chunk = ''.join(self._data[:dims[0]])
            self._data = self._data[dims[0]:]

            self._decompressed += chunk*dims[1]
        else:
            self._decompressed += self._data[0]
            self._data = self._data[1:]

    def part1(self):
        with open(self._fn, 'r') as f:
            self._data = [x for x in f.read() if not x.isspace()]
        self._decompressed = ""

        while (len(self._data)):
            self._parse()

        return len(self._decompressed)

    def _part2(self):
        dims = self._parse_compression()
        chunk = ''.join(self._data[:dims[0]])
        if '(' in chunk:
            print(len(chunk), end=' ')
            dims, read = self._parse_chunk(chunk)
        print(chunk, dims, read)
        quit()

    def part2(self):
        with open(self._fn, 'r') as f:
            self._data = [x for x in f.read() if not x.isspace()]

        self._d_size = 0

        while len(self._data):
            if self._data[0] == '(':
                self._part2()
            else:
                self._d_size += 1
                self._data = self._data[1:]

        return self._d_size


if __name__ == '__main__':
    puzzle = Puzzle("test.txt")
    print(f"Part 1: {puzzle.part1()}")
    print(f"Part 2: {puzzle.part2()}")

# END OF FILE
