
# `` Day 5
# * url to puzzle: https://adventofcode.com/2022/day/5

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

#         [H]     [W] [B]
#     [D] [B]     [L] [G] [N]
# [P] [J] [T]     [M] [R] [D]
# [V] [F] [V]     [F] [Z] [B]     [C]
# [Z] [V] [S]     [G] [H] [C] [Q] [R]
# [W] [W] [L] [J] [B] [V] [P] [B] [Z]
# [D] [S] [M] [S] [Z] [W] [J] [T] [G]
# [T] [L] [Z] [R] [C] [Q] [V] [P] [H]
#  1   2   3   4   5   6   7   8   9


stacks = {
    "1": ['T', 'D', 'W', 'Z', 'V', 'P'],
    "2": ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
    "3": ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
    "4": ['R', 'S', 'J'],
    "5": ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
    "6": ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
    "7": ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
    "8": ['P', 'T', 'B', 'Q'],
    "9": ['H', 'G', 'Z', 'R', 'C'],
}


def moves(data):
    for line in data:
        line = line.split(' ')
        amount = line[1]
        source = line[3]
        dest = line[5]
        # transfer(int(amount), source, dest)
        transfer_part2(int(amount), source, dest)


def transfer(amt, src, dest):
    for i in range(amt):
        stacks[dest].append(stacks[src].pop())
        
def transfer_part2(amt,src,dest):
    stacks[dest] += stacks[src][amt*-1:]
    del stacks[src][amt*-1:]


def print_end():
    print('PRINTING:')
    for stack in stacks.keys():
        print(stacks[stack][-1])


def main():
    data = read_file('input.txt')
    moves(data)
    print_end()
    

if __name__ == "__main__":
    main()
