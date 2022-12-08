
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
    max_score = 0
    j = 0
    col = np.rot90(lines)
    for line in lines:
        n = len(line)
        for tree in range(n):  
            # print(line)  
            right = 1
            left = 1
            up = 1
            down = 1
            for i in range(tree+1, n):
                if(line[i] < line[tree]):
                    right += 1
                    break
            for i in range(0, tree-1):
                if(line[i] < line[tree]):
                    left += 1
                    break
            for i in range(j+1, n):
                if(col[j-tree][i] < line[tree]):
                    up +=1
                    break
            for i in range(0, j-1):
                if(col[j-tree][i] < line[tree]):
                    down +=1
                    break
            score = left*right*up*down
            if score > max_score:
                max_score = score
        #     # print(i)
        #     if tree == 0 or tree == n-1 or i == 0 or i == n-1:
        #         vision += 1                      
        #     elif (all(line[tree] > line[:tree]) or all(line[tree] > line[tree+1:])):
        #         vision += 1
        #         # print('row:',line, tree)
        #     elif (all(line[tree] > col[:i]) or all(line[tree] > col[i+1:])):
        #         vision += 1
        #         # print('col:',line, col, tree,i)
        #         # print(col, i)
        j += 1
        # j = 0
    print('max score',max_score)#+(2*lines.shape[0])-4)


if __name__ == "__main__":
    main()
