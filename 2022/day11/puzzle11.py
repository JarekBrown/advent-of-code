
# `` Day 11
# * url to puzzle: https://adventofcode.com/2022/day/11

import re
import gmpy2 as gm


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
    return [i.strip('\n').strip() for i in data]

def start_items(data):
    monkeys = {}
    curr = ''
    for line in data:
        if(line == ''):
            continue
        line = re.sub(',|:','',line).split()
        if line[0] == 'Monkey':
            curr = line[1]
            monkeys[curr] = [None]*5
        elif line[0] == 'Starting':
            monkeys[curr][0] = [int(x) for x in line[2:]]
        elif line[0] == 'Operation':
            monkeys[curr][1] = line[4:]
        elif line[0] == 'Test':
            monkeys[curr][2] = int(line[3])
        elif line[1] == 'true':
            monkeys[curr][3] = line[5]
        elif line[1] == 'false':
            monkeys[curr][4] = line[5]
    return monkeys

def operation(operator, val, inc):
    val = int(val)
    if inc == 'old':
        inc = val
    inc = int(inc)
    match operator:
        case '+':
            return gm.add(val,inc)
        case '*':
            return gm.mul(val,inc)

def process(monkeys,counts,mod_val):
    pos = 0
    for monkey in monkeys:
        operate = monkeys[monkey][1]
        test = monkeys[monkey][2]
        t = monkeys[monkey][3]
        f = monkeys[monkey][4]
        for i in monkeys[monkey][0]:
            counts[pos] += 1
            worry = operation(operate[0],i,operate[1]) % mod_val #* used for part 1: // 3
            if worry % test == 0:
                monkeys[t][0].append(worry)
            else:
                monkeys[f][0].append(worry)
        monkeys[monkey][0] = []
        pos += 1
    return monkeys,counts
    
def print_monkeys(monkeys,round):
    print('After round {}, the monkeys are holding the following:'.format(round))
    for monkey in monkeys:
        print('Monkey {}: {}'.format(monkey, monkeys[monkey][0]))
                
def loop(monkeys,rounds,mod_val):
    count = [0]*len(monkeys)
    for _ in range(rounds):
        monkeys,count = process(monkeys,count,mod_val)
    count.sort(reverse=True)
    level = count[0] * count[1]
    return level       

def find_mod(monkeys):
    val = 1
    for monkey in monkeys:
        val *= monkeys[monkey][2]
    return val 

if __name__ == "__main__":
    data = read_file('input.txt')
    monkeys = start_items(data)
    mod_val = find_mod(monkeys)
    print('Level for da monkeys: ', loop(monkeys,10000,mod_val))

