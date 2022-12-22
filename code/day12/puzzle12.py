
# `` Day 12
# * url to puzzle: https://adventofcode.com/2022/day/12

import numpy as np


def read_file(filename):
    """reads in text file data

    Args:
        filename (str): name of input file
    Returns:
        data (list): list of each line in file
    """
    file = open(filename, "r")
    data = file.readlines()
    file.close()
    return [i.strip('\n').strip() for i in data]


def convert(data, elevations):
    layout = np.zeros((len(data), len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[i])):
            layout[i][j] = elevations[data[i][j]]
    return layout


def valid_moves(pos, layout):
    print(pos)
    print(layout)
    x = pos[0]
    y = pos[1]
    limx, limy = layout.shape
    curr_val = layout[x][y]
    # print(curr_val)
    # print(layout[2][3])
    moves = []
    down = x+1
    up = x-1
    right = y+1
    left = y-1
    if right <= limx and layout[x][right] - 1 <= curr_val:
        # print('right: ',right, layout[x][right])
        moves.append([x, right])
    if left >= 0 and layout[x][left] - 1 <= curr_val:
        # print('left: ', layout[x][left])
        moves.append([x, left])
    if up >= 0 and layout[up][y] - 1 <= curr_val:
        # print('up: ', layout[up][y])
        moves.append([up, y])
    if down <= limy and layout[down][y] - 1 <= curr_val:
        # print('down: ', layout[down][y])
        moves.append([down, y])
    return moves


def travel(prev, curr, steps, layout):
    print(curr)
    steps += 1
    if layout[curr[0]][curr[1]] == 1000:
        return steps
    moves = valid_moves(curr,layout)
    if prev in moves:
        moves.remove(prev)
    counts = []
    for move in moves:
        counts.append(travel(curr, move, steps, layout))
    return min(counts)


if __name__ == "__main__":
    data = read_file('test.txt')
    elevations = {chr(i+96): i for i in range(1, 27)}
    elevations['S'] = 0
    elevations['E'] = 1000
    layout = convert(data, elevations)
    steps = travel(None, [2,2],0,layout)
    print(steps)
    # print(valid_moves([1, 1], layout))
