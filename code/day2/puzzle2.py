
# `` Day 2
# * url to puzzle: https://adventofcode.com/2022/day/2

def score(opponent, player):
    """scores the outcomes of a round of rock paper scissors

    Args:
        opponent (str): opponent's action
        player (str): player's action
    Returns:
        0 if lo
    """
    # A/X:Rock, B/Y:Paper, C/Z:Scissors PART 1
    # X: lose, Y: draw, Z: win
    score = 0
    match player:
        case "X":
            # score = 1
            # if(opponent == "A"):
            #     score += 3
            # elif(opponent == "C"):
            #     score += 6
            if(opponent == "A"):
                score = 3
            elif(opponent == "B"):
                score = 1
            else:
                score = 2
        case "Y":
            # score = 2
            # if(opponent == "B"):
            #     score += 3
            # elif(opponent == "A"):
            #     score += 6
            if(opponent == "A"):
                score = 4
            elif(opponent == "B"):
                score = 5
            else:
                score = 6
        case "Z":
            # score = 3
            # if(opponent == "C"):
            #     score += 3
            # elif(opponent == "B"):
            #     score += 6
            if(opponent == "A"):
                score = 8
            elif(opponent == "B"):
                score = 9
            else:
                score = 7
    return score

def read_file(filename):
    """reads in text file data

    Args:
        filename (str): name of input file
    Returns:
        data (list): list of each line in file
    """
    file = open(filename, "r")
    data = file.readlines()
    return [i.strip('\n') for i in data]

def main():
    data = read_file('input.txt')
    scores = [0]
    i = 0
    for datum in data:
        datum = datum.split()
        scores[i] = score(datum[0], datum[1])
        i += 1
        scores.append(0)
    print(sum(scores))

if __name__ == "__main__":
    main()