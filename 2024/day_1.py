"""
Advent of Code 2024
Day 1
Author: James M. Horne
"""
from collections import Counter, defaultdict

if __name__ == '__main__':
    with open(file='1.data', encoding='utf-8') as f:
        data = f.read()

    # test data
    # data = '''3   4
    # 4   3
    # 2   5
    # 1   3
    # 3   9
    # 3   3'''

    data = [[int(y) for y in x.split('   ')] for x in data.split('\n')]
    first = [x[0] for x in data]
    second = [x[1] for x in data]
    first.sort()
    second.sort()

    # part 1
    ans = sum((abs(first[x] - second[x]) for x in range(len(first))))
    print(f"Part 1: {ans}")

    # part 2
    count = defaultdict(int, Counter(second))
    ans = sum((x * count[x] for x in first))
    print(f"Part 2: {ans}")
