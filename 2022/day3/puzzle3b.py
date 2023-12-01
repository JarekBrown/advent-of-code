
# `` Day 3 - puzzle 2
#* url to puzzle: https://adventofcode.com/2022/day/3#part2

def read_file(filename):
    """reads in text file data

    Args:
        filename (str): name of input file
    Returns:
        data (list): list of each line in file
    """
    file = open(filename, "r")
    file.close()
    data = file.readlines()
    return [i.strip('\n') for i in data]

def common_letter(elf1, elf2, elf3):
    """finds the common letter in the candies

    Args:
        elf1 (str): first elf 
        elf2 (str): second elf
        elf3 (str): third elf
    """
    for group in elf1:
        if group in elf2 and group in elf3:
            return group

def common_item(sacks):
    """finds the common item present in each of the three-elf groups

    Args:
        sacks (list): rucksacks read from input
    """
    elfies = []
    for pos in range(0,len(sacks),3):
        elfies.append(common_letter(sacks[pos],sacks[pos+1],sacks[pos+2]))
    return elfies

def prioritize(mistakes):
    """sets the priority of each mistake

    Args:
        mistakes (list): all the found mistakes
    """
    priority = {chr(i+96):i for i in range(1,27)}
    priority.update({k.upper(): i+26 for k,i in priority.items()})
    val = []
    for candy in mistakes:
        val.append(priority[candy])
    return val
    

def main():
    data = read_file('input.txt')
    candies = common_item(data)
    nums = prioritize(candies)
    print(sum(nums))
    
    
if __name__ == "__main__":
    main()