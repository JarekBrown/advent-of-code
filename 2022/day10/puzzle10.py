
# `` Day 10
# * url to puzzle: https://adventofcode.com/2022/day/10

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


def execution(program):
    cycle = 1
    x = 1
    signal = []
    x_val = []
    for line in program:        
        line = line.split()
        if line[0] == 'addx':
            for _ in range(2):
                x_val.append(x)
                signal.append(cycle * x)
                cycle += 1
            x += int(line[1])
        else:
            x_val.append(x)
            signal.append(cycle * x)
            cycle += 1   
    return signal,x_val

# part 1
def sig_sum(signals):
    i = 20
    sig_sum = 0
    while i < 221:
        sig_sum += signals[i-1]
        i += 40
    print(sig_sum)
        

# part 2
def crt(x):
    screen = np.zeros([6,41])
    screen[0][0]=1
    row = 0
    spot = 1
    for i in range(1,len(x)-1):
        if (i%40 == 0):
            spot = 0
            row += 1
        pos = x[i]
        if ((spot==pos) or (spot==(pos-1)) or (spot==(pos+1))): 
            screen[row][spot] = 1         
        spot += 1
    for i in range(6):
        line = ''
        for j in range(40):
            if screen[i][j] == 1:
                line += '#'
            else:
                line += '.'
        print(line)
            


def main():
    data = read_file('input.txt')
    signals,xs = execution(data)
    print('-'*50)
    print('*'*10,'PART 1','*'*10)
    sig_sum(signals)
    print('-'*50)
    print('*'*10,'PART 2','*'*10)
    crt(xs)    
    print('-'*50)


if __name__ == "__main__":
    main()
