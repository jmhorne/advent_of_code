#!/usr/bin/env python3

class Puzzle:
    def __init__(self, input_filename):
        self._ins = self._parse_input(input_filename)
        self._pos = [0, 0]
        self._visited = [[0, 0]]
        self._dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]] # NESW
        self._dir = 0

        for i in self._ins:
            i[0]()

            for _ in range(i[1]):
                self._pos[0] += self._dirs[self._dir][0]
                self._pos[1] += self._dirs[self._dir][1]
                self._visited.append(self._pos.copy())

    def _parse_input(self, filename):
        func_keys = {'R': self._turn_right, 'L': self._turn_left}
        with open(filename, 'r') as f:
            return [[func_keys[x[0]], int(x[1])] for x in f.read().split(', ')]

    def _turn_left(self):
        print('left', self._dir, end=' ')
        self._dir = (self._dir - 1) % 4
        print(self._dir)
        # print('left', self._dir, end=' ')
        # self._dir -= 1#
        # print(self._dir, end=' ')
        # self._dir = self._dir % 4
        # print(self._dir, self._dirs[self._dir])

    def _turn_right(self):
        print('right', self._dir, end=' ')
        self._dir = (self._dir + 1) % 4
        print(self._dir)
        # print('right', self._dir, end=' ')
        # self._dir += 1#
        # print(self._dir, end=' ')
        # self._dir = self._dir % 4
        # print(self._dir, self._dirs[self._dir])

    def part1(self):
        return abs(0 - self._visited[-1][0]) + abs(0 - self._visited[-1][1])



if __name__ == '__main__':
    p = Puzzle("test.txt")
    print(p.part1())
    print(p._visited, len(p._visited))

# END OF FILE
