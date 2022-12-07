
# `` Day 7
# * url to puzzle: https://adventofcode.com/2022/day/7

from collections import defaultdict


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

def sum_it_all(sizes):
    sum = 0
    options = []
    update_size = 30000000 - (70000000 - list(sizes)[0])
    for size in sizes:
        if size <= 100000:
            sum += size
        elif size >= update_size:
            options.append(size)
    print('SUM THEM MOTHER*******: ', sum)
    print('BURN THIS **** AT LEAST:', min(options))

def main():
    data = read_file('input.txt')
    file_sys = {}
    path=[]
    
    for line in data:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":                
                if line[2] == "..":
                    path.pop()
                else:
                    path.append(line[2])
        elif not(line[0] == "dir"):
            for i in range(len(path)):
                if not(tuple(path[:i+1]) in file_sys.keys()):
                    file_sys[tuple(path[:i+1])] = 0
                file_sys[tuple(path[:i+1])] += int(line[0])
    sum_it_all(file_sys.values())
    

if __name__ == "__main__":
    main()