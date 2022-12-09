
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

def movements(data):
    visited = []
    h = 0
    t = 0    
    directions = {'R':1,'U':1j,'L':-1,'D':-1j}
    for line in data:
        # print(move)
        line = line.split()
        direction = directions[line[0]]
        dist = int(line[1])
        for i in range(dist):
            h += direction
            d = h-t 
            if(d.real >= -2 and d.real <= 2 and d.imag >= -2 and d.imag <= 2):
                t += d/2
            elif(d.real == 0 and d.imag == 0):
                continue
            elif(d.real == 0 and abs(d.imag) == 1):
                continue
            elif(abs(d.real) == 1 and d.imag == 0):
                continue
            else:
                t += d
        visited.append(t)
                
    print(len(visited))
    
def main():
    test_file = read_file('test.txt')
    data = read_file('input.txt')
    movements(test_file)
    # movements(data)
    


if __name__ == "__main__":
    main()
