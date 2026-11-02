#!/usr/bin/env python3

'''TODO'''

PUZZLE_FILENAME = "input.txt"
PUZZLE_INPUT = []

def rotate_keypad(keypad:list[list[int]], clockwise=True) -> list[list[int]]:
    if clockwise:
        return [list(row) for row in zip(*keypad[::-1])]
    else:
        return [list(row) for row in zip(*keypad)][::-1]


def rotate_row(keypad, row, amount):
    keypad[row] = keypad[row][-amount:] + keypad[row][:-amount]
    return keypad


def rotate_column(keypad, col, amount):
    keypad = rotate_keypad(keypad, False)

    col = len(keypad) - (col + 1)
    keypad[col] = keypad[col][-amount:] + keypad[col][:-amount]

    return rotate_keypad(keypad)


def fill_rect(keypad, width, height):
    for y in range(min(height, len(keypad))):
        for x in range(min(width, len(keypad[y]))):
            keypad[y][x] = 1
    return keypad


def parse_puzzle_input():
    with open(PUZZLE_FILENAME, 'r') as f:
        raw = [x.split(' ') for x in f.read().split('\n')]

    func_keys = {'column': rotate_column, 'row': rotate_row}

    for r in raw:
        if len(r) == 2:
            i = [fill_rect] + [int(x) for x in r[1].split('x')]
        else:
            i = [func_keys[r[1]], int(r[2].split('=')[1]), int(r[4])]
        PUZZLE_INPUT.append(i)


def create_keypad(width, height):
    keypad = []
    for _ in range(height):
        keypad.append([0]*width)
    return keypad


def show_keypad(keypad):
    box = '\u2588'

    for row in keypad:
        for col in row:
            if col == 1:
                print(box, end='')
            else:
                print(' ', end='')
        print()
    print()


def keypad_value(keypad) -> int:
    return sum([sum(x) for x in keypad])


def part1():
    parse_puzzle_input()
    keypad = create_keypad(50, 6)

    for i in PUZZLE_INPUT:
        keypad = i[0](keypad, i[1], i[2])

    print(f"Part 1: {keypad_value(keypad)}")
    print("Part 2:")
    show_keypad(keypad)

if __name__ == '__main__':
    part1()

# END OF FILE
