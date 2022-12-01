
# `` Day 1
# * url to puzzle: https://adventofcode.com/2022/day/1


def read_file(filename):
    """reads in text file data

    Args:
        filename (str): name of input file
    Returns:
        data (list): list of each line in file
    """
    file = open(filename, "r")
    data = file.readlines()
    return data

def sum_data(values):
    """sums each grouping of numbers

    Args:
        values (list): data returned by `read_file` function
    """
    sums = [0]
    i = 0
    for val in values:
        val = val.strip() # removes \n char
        if val == '':
            i += 1
            sums.append(0)
            continue
        else:
            sums[i] += int(val)
    return sums
            
            
def main():
    nums = read_file("input.txt")
    sums = sum_data(nums)
    sums.sort(reverse=True)
    print('top three: ', sums[:3])
    print('sum of top three: ', sum(sums[:3]))
    
if __name__ == "__main__":
    main()