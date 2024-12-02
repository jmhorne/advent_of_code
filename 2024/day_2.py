"""
Advent of Code 2024
Day 2
Author: James M. Horne
"""

def get_dif(l:int, r:int) -> tuple:
    """
    Returns the difference value of two numbers and
        whether that it is increasing or decreasing form left to right

    l: left value
    r: right value

    returns a tuple with results
    """
    dif = l - r
    is_increasing = dif > 0

    return abs(dif), is_increasing

def is_safe(report:list, part2:bool=False) -> int:
    """
    Determines if a report is safe

    report: report to test
    part2: flag that determines part2 logic should be used

    returns 0 if not safe and 1 if safe
    """
    _, last = get_dif(report[0], report[1])

    for x in range(len(report) - 1):
        dif, iinc = get_dif(report[x], report[x + 1])

        if dif > 3 or dif == 0 or iinc != last:
            if part2:
                return is_safe_with_removal(report)

            return 0

    return 1

def is_safe_with_removal(report:list) -> int:
    """
    determines if a report is safe if levels are removed from a report

    report: report to test

    returns 0 if not safe and 1 if safe
    """
    for x in range(len(report)):
        temp = report[0:x] + report[x+1:]
        if is_safe(temp):
            return 1
    return 0

if __name__ == '__main__':
    with open(file='2.data', encoding='utf-8') as f:
        data = f.read()

    # # Test data
    # data = '''7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9'''

    reports = [[int(y) for y in x.split(' ')] for x in data.split('\n')]

    # part 1
    ans = sum((is_safe(x) for x in reports))
    print(f"Part 1: {ans}")

    # part 2
    ans = sum((is_safe(x, True) for x in reports))
    print(f"Part 2: {ans}")
