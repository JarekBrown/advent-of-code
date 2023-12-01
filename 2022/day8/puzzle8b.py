
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

def scenic(data):
    tmp = []
    for line in data:
        tmp.append([int(i) for i in line])
    lines = np.asarray(tmp)
    j = 0
    col = np.rot90(lines)
    col = col[::-1]
    scores = []
    for line in lines:
        n = len(line)
        for tree in range(n):  
            if j == 0 or j == n-1 or tree == 0 or tree == n-1:
                score = 0
            else: 
                right = 0
                left = 0
                up = 0
                down = 0
                pos = [line[:tree],line[tree+1:], col[tree][:j], col[tree][j+1:]]
                for i in np.flip(pos[0]):
                    left += 1
                    if(i >= line[tree]):
                        break
                for i in pos[1]:
                    right += 1
                    if(i >= line[tree]):
                        break
                for i in np.flip(pos[2]):
                    up +=1
                    if(i >= line[tree]):
                        break
                for i in pos[3]:     
                    down +=1
                    if(i >= line[tree]):
                        break
                score = left*right*up*down
            scores.append(score)
        j += 1
    return(np.max(scores))

def main():
    data = read_file('test.txt')
    print('test file: ', scenic(data))
    data = read_file('input.txt')
    print('input file: ', scenic(data))
    


if __name__ == "__main__":
    main()
