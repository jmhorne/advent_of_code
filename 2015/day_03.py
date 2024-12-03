"""
Advent of Code 2015
Day 3
Author: James M. Horne
"""

def travel(travel_map:str) -> list:
    """
    Follows the travel map and returns a set of visited homes

    travle_map: string of directions

    returns a list of visited home positions
    """
    x = 0
    y = 0
    visited = [(x, y)]

    for d in travel_map:
        if d == "^":
            y -= 1
        elif d == ">":
            x += 1
        elif d == "<":
            x -= 1
        else: # "v"
            y += 1

        visited.append((x, y))

    return list(set(visited))

if __name__ == '__main__':
    with open(file='puzzle_input/3', encoding='utf-8') as f:
        puzzle = f.read()

    print(f"Part 1: {len(travel(puzzle))}")
    print(f"Part 2: {len(set(travel(''.join([puzzle[x] for x in range(0, len(puzzle), 2)])) + travel(''.join([puzzle[x] for x in range(1, len(puzzle), 2)]))))}")