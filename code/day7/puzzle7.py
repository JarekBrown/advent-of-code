
# `` Day 7
# * url to puzzle: https://adventofcode.com/2022/day/7

file_sys = {}
path = []

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

def update_size(curr, size):
    # print('HERE',curr)
    file_sys[curr][1] += size
    # while curr != "/":
    #     curr = file_sys[curr][0]
    #     # print(file_sys)
    #     file_sys[curr][1] += size

def system_size(data):
    curr = ''
    for line in data:
        # print(line)
        line = line.split(' ')
        if line[0] == "$" and line[1] == "cd":
            print(line)
            if line[2] == "..":
                if curr == "/":
                    continue;
                curr = file_sys[curr][0]
            elif line[2] == ".":
                continue;
            elif line[2] == "/":
                file_sys[line[2]] = [None, 0]
                curr = line[2]
            else:
                if not(line[2] in file_sys.keys()):
                    file_sys[line[2]] = [curr, 0]
                curr = line[2]
        elif line[0].isnumeric():
            update_size(curr,int(line[0]))  
            
def update_post():
    keys = list(reversed(sorted(file_sys.keys())))
    print(keys)
    for folder in keys:
        print('FOLDER: ',folder)
        tmp = file_sys[folder][0]
        print(tmp)
        print(file_sys[folder][1])  
             
        if tmp == None:
            break;
        print('before: ', file_sys[tmp][1]) 
        file_sys[tmp][1] += file_sys[folder][1]
        print('after: ', file_sys[tmp][1]) 
                    
    
def size_sum():
    sum = 0
    for folder in file_sys:
        tmp = file_sys[folder][1]
        print('maybe',tmp)
        if(tmp <= 100000):
            sum += tmp
            print('progress', sum)
    return sum

def main():
    data = read_file('input.txt')
    system_size(data)
    update_post()
    size = size_sum()
    print(size)
    # print(3000000)
    # print(file_sys)
    

if __name__ == "__main__":
    main()