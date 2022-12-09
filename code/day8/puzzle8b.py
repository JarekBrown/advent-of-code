
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
    max_score = 1
    j = 0
    col = np.rot90(lines)
    col = col[::-1]
    scores = []
    # print(lines)
    for line in lines:
        n = len(line)
        for tree in range(n):  
            # print(tree) 
            # print(col)
            # print(col[(tree)],j) 
            right = 0
            left = 0
            up = 0
            down = 0
            pos = [line[tree-1::],line[tree+1:], col[tree][j-1::], col[tree][j+1:]]
            # print(pos[0],pos[1],pos[2],pos[3])
            for i in pos[0]:
                # print(i)
                if(i >= line[tree]):
                    break
                left += 1
                    # break
                # print('left:',left)
            for i in pos[1]:
                if(i >= line[tree]):
                    break
                right += 1
                    # break
                # print('right :',right)
            for i in pos[2]:
                if(i >= line[tree]):
                    break
                up +=1
                # print('up:',up)
                    # break
            for i in pos[3]:                
                # print(col[j-tree][i], line[tree])
                # print(i)
                if(i >= line[tree]):
                    break
                    # print('yes')
                down +=1
                # print('down:',down)
                    # break
            # print('down',down)
            score = left*right*up*down
            scores.append(score)
            # print(score,right,left,up,down, max_score)
            # if score >= max_score:
            #     max_score = score
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
    print(j)
    return(np.max(scores))

def main():
    data = read_file('input.txt')
    print(scenic(data))
    


if __name__ == "__main__":
    main()
