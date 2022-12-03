
# `` Day 3
#* url to puzzle: https://adventofcode.com/2022/day/3

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

def common_letter(candy1, candy2):
    """finds the common letter in the candies

    Args:
        candy1 (str): first item 
        candy2 (str): second item
    """
    for sugar in candy1:
        if sugar in candy2:
            return sugar

def common_item(sacks):
    """finds the common item present in each of the two items present in each rucksack

    Args:
        sacks (list): rucksacks read from input
    """
    elf_mistakes = []
    for ruck in sacks:
        n = len(ruck)
        elf_mistakes.append(common_letter(ruck[0:n//2],ruck[n//2:]))
    return elf_mistakes

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