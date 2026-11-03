#!/usr/bin/env python3

class Puzzle:
    def __init__(self, input_filename):
        with open(input_filename, 'r') as f:
            self._raw = f.read().strip()

    def _parse(self):
        self._chunk = self._chunk[1:]
        dims = ""

        while self._chunk[0] != ')':
            dims += self._chunk[0]
            self._chunk = self._chunk[1:]
        self._chunk = self._chunk[1:]

        dims = [int(x) for x in dims.split('x')]
        return dims[0], dims[1]

    def _build_chunks(self, chunk:list[str]=None, nested=False):
        if chunk:
            self._chunk = chunk
        else:
            self._chunk = self._raw

        chunks = []

        while len(self._chunk):
            if '(' not in self._chunk:
                i = len(self._chunk)
            else:
                i = self._chunk.index('(')

            if i > 0:
                chunks.append([1, self._chunk[:i]])
                self._chunk = self._chunk[i:]
                continue

            cnt, rpt = self._parse()
            chunks.append([rpt, self._chunk[:cnt]])
            self._chunk = self._chunk[cnt:]

        if nested:
            for i, c in enumerate(chunks):
                if '(' in c[1]:
                    chunks[i][1] = self._build_chunks(c[1], nested)

        return chunks

    def _sum_chunk(self, chunk):
        if isinstance(chunk[1], list):
            s = sum([self._sum_chunk(x) for x in chunk[1]])
        else:
            s = len(chunk[1])

        return chunk[0] * s

    def part1(self):
        return sum([self._sum_chunk(x) for x in self._build_chunks()])

    def part2(self):
        return sum([self._sum_chunk(x) for x in self._build_chunks(nested=True)])


if __name__ == '__main__':
    puzzle = Puzzle("input.txt")
    print(f"Part 1: {puzzle.part1()}")
    print(f"Part 2: {puzzle.part2()}")

# END OF FILE
