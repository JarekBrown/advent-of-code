
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

def signal_start(stream):
    signals = []
    count = 0
    for line in stream:
        for char in line:
            count += 1
            signals.append(char)
            if len(signals) == 14:
                if len(set(signals)) == 14:
                    return count
                else:
                    signals.pop(0)
            


def main():
    data = read_file('input.txt')
    print(signal_start(data))
    
    
if __name__ == "__main__":
    main()