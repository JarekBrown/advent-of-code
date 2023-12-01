
# `` Day 8
# * url to puzzle: https://adventofcode.com/2022/day/8

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
    return [i.strip('\n') for i in data]

def main():
    data = read_file('input.txt')
    tmp = []
    for line in data:
        tmp.append([int(i) for i in line])
    lines = np.asarray(tmp)
    vision = 0
    record = {}
    i = 0
    for line in lines:
        n = len(line)
        for tree in range(n): 
            # print(line)           
            col = lines[:, tree]
            # print(i)
            if tree == 0 or tree == n-1 or i == 0 or i == n-1:
                vision += 1                      
            elif (all(line[tree] > line[:tree]) or all(line[tree] > line[tree+1:])):
                vision += 1
                # print('row:',line, tree)
            elif (all(line[tree] > col[:i]) or all(line[tree] > col[i+1:])):
                vision += 1
                # print('col:',line, col, tree,i)
                # print(col, i)
        i += 1
        # i = 0
    print(vision)#+(2*lines.shape[0])-4)


if __name__ == "__main__":
    main()
