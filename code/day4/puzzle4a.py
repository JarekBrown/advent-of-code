
# `` Day 4
#* url to puzzle: https://adventofcode.com/2022/day/4

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

def check_pairs(line):
    """checks if the pairs of elves are fully duplicating work

    Args:
        line (str): single line of file
    """
    elves = line.split(',')
    elf1 = [int(i) for i in elves[0].split('-')]
    elf2 = [int(i) for i in elves[1].split('-')]
    if(elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
        return 1
    if(elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        return 1
    else:
        return 0
    
def lucky_elves(pairs):
    """counts the number of lucky elves that don't need to do work

    Args:
        pairs (list): all the pairs of elves
    """
    lucky = 0
    for pair in pairs:
        lucky += check_pairs(pair)
    print('There were ', lucky, ' lucky elves!')

def main():
    data = read_file('input.txt')
    lucky_elves(data)
    # print(check_pairs('2-8,3-7'))
    
    
if __name__ == "__main__":
    main()