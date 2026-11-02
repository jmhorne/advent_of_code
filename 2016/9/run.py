#!/usr/bin/env python3

import re

class Puzzle:
    def __init__(self, input_filename):
        self._fn = input_filename

    def _parse_compression(self):
        dims = ""

        self._data = self._data[1:]
        while self._data[0] != ')':
            dims += self._data[0]
            self._data = self._data[1:]
        self._data = self._data[1:]

        dims = [int(x) for x in dims.split('x')]
        return dims
        # chunk = ''.join(self._data[:dims[0]])
        # self._data = self._data[dims[0]:]

        # self._decompressed += chunk*dims[1]

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
        print(dims)
        print(self._data[:10])
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

        # self._data = list(self._decompressed)
        # self._decompressed = ""

        # while (len(self._data)):
        #     self._parse()

        # pattern = r"\(\d+x\d+\)"
        # if len(re.findall(pattern, self._decompressed)) > 0:
        #     print(f"{len(self._decompressed):,}")
        #     self.part2()

        # return len(self._decompressed)

        # with open(self._fn, 'r') as f:
        #     data = f.read()

        # pattern = r"\(\d+x\d+\)"

        # matches = re.findall(pattern, data)
        # decompressed_size = 0

        # print(matches[-1])


if __name__ == '__main__':
    puzzle = Puzzle("test.txt")
    print(f"Part 1: {puzzle.part1()}")
    print(f"Part 2: {puzzle.part2()}")

# END OF FILE
