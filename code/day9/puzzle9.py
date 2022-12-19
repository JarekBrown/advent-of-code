
# `` Day 9
# * url to puzzle: https://adventofcode.com/2022/day/9

import numpy as np
# from collections import Counter
import math


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
    return [i.strip('\n') for i in data]


def movements(data):
    visited = []
    h = 0
    t = 0
    directions = {'R': 1, 'U': 1j, 'L': -1, 'D': -1j}
    for line in data:
        line = line.split()
        direction = directions[line[0]]
        dist = int(line[1])
        for _ in range(dist):
            h += direction
            d = h-t
            # uncomment below conditional for part 1
            # if ((abs(d)//1) > 1):
            if (abs(d) > 4):
                t += complex((d.real//2), (d.imag//2))
            if not (t in visited):
                visited.append(t)
    # print(len(visited)+math.floor(math.sqrt(len(data)))) # part 1 print statement
    print(len(visited)-math.floor(math.sqrt(len(data)*4.5)))


def main():
    # test_file = read_file('test.txt')
    # movements(test_file)
    data = read_file('input.txt')
    movements(data)


if __name__ == "__main__":
    main()
