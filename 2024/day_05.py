"""
Advent of Code 2024
Day 5
Author: James M. Horne
"""

from collections import defaultdict
from math import floor

def parse_ordering(raw:str) -> defaultdict:
    """
    Parses raw orderings into a dictionary for quick lookup

    raw: string containing ordering

    returns defaultdict with pages and their dependencies
    """
    raw = raw.split('\n')
    ordering = defaultdict(list)

    for row in raw:
        f, s = row.split('|')
        ordering[s].append(f)

    return ordering

def test_update(update, orders) -> tuple:
    """
    Tests an updates validity and returns its middle number. if invalid, corrects it

    update: update to test
    orders: ordering rules

    returns:
        if update is valid, return tuple with first element being update's middle number
            and second element being 0
        if update is invalid, correct it, then return tuple with first element being 0
            and second element being update's middle number
    """
    for idx, u in enumerate(update):
        for o in orders[u]:
            if o in update and o not in update[:idx]:
                correct_update(update, orders)
                return 0, int(update[floor(len(update)/2)])

    return int(update[floor(len(update)/2)]), 0

def correct_update(incorrect, orders):
    """
    Corrects an update based on order rules

    incorrect: update to correct
    orders: ordering rules
    """
    for idx, u in enumerate(incorrect):
        for o in orders[u]:
            if o in incorrect and o not in incorrect[:idx]:
                pos = incorrect.index(o)
                incorrect[idx], incorrect[pos] = incorrect[pos], incorrect[idx]
                return correct_update(incorrect, orders)

if __name__ == '__main__':
    with open('puzzle_input/5', encoding='utf-8') as f:
        puzzle = f.read()

    ordering, updates = puzzle.split('\n\n')
    ordering = parse_ordering(ordering)
    updates = [x.split(',') for x in updates.split('\n')]

    results = [test_update(update, ordering) for update in updates]
    print(f"Part 1: {sum((x[0] for x in results))}")
    print(f"Part 2: {sum((x[1] for x in results))}")
