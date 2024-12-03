"""
Advent of Code 2015
Day 1
Author: James M. Horne
"""

def needed(dimensions:str) -> tuple:
    """
    Given a gifts dimensions, determines how much wrapping paper and ribbon is required

    dimensions: string representation of a gift's dimensions

    returns how much wrapping paper and ribbon is needed
    """
    dims = [int(x) for x in dimensions.split('x')]
    l, w, h = dims

    # solve wrap needed
    wrap_raw = [l * w, w * h, h * l]
    wrap = min(wrap_raw) + sum((x * 2) for x in wrap_raw)

    # solve ribbon needed
    dims.sort()
    ribbon = (2 * dims[0]) + (2 * dims[1]) + (dims[0] * dims[1] * dims[2])

    return wrap, ribbon

if __name__ == '__main__':
    with open(file='puzzle_input/2', encoding='utf-8') as f:
        puzzle = f.readlines()

    # print(sum((wrapping_needed(x) for x in puzzle)))
    needs = [needed(x) for x in puzzle]

    print(f"Part 1: {sum((x[0] for x in needs))}")
    print(f"Part 2: {sum((x[1] for x in needs))}")
