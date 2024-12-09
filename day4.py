# Read in a text file, each row should be a list of characters

def read_file(file_path):
    l = []
    with open(file_path, 'r') as file:
        for line in file:
            l.append(list(line.strip()))
    
    # add 3 padding to the top / bottom / left / right with a "." as the padding character
    l = [['.'] * (len(l[0]) + 6)] * 3 + [['.'] * 3 + row + ['.'] * 3 for row in l] + [['.'] * (len(l[0]) + 6)] * 3
    return l

# Part 1
print("part 1")


# search for the word XMAS. It can appear up / down, left / right or diagonally
# if it is found, add it to a running total of the number of times it appears
def part1(lists):       
    total = 0
    for i in range(3,(len(lists)-3)):
        for j in range(3,(len(lists[i])-3)):
            if lists[i][j] == 'X':
                # check up
                if (lists[i-1][j] + lists[i-2][j] + lists[i-3][j]) == 'MAS':
                    total += 1
                # check down
                if (lists[i+1][j] + lists[i+2][j] + lists[i+3][j]) == 'MAS':
                    total += 1
                # check left
                if (lists[i][j-1] + lists[i][j-2] + lists[i][j-3]) == 'MAS':
                    total += 1
                # check right
                if (lists[i][j+1] + lists[i][j+2] + lists[i][j+3]) == 'MAS':
                    total += 1
                # check diagonally up left
                if (lists[i-1][j-1] + lists[i-2][j-2] + lists[i-3][j-3]) == 'MAS':
                    total += 1
                # check diagonally up right
                if (lists[i-1][j+1] + lists[i-2][j+2] + lists[i-3][j+3]) == 'MAS':
                    total += 1
                # check diagonally down left
                if (lists[i+1][j-1] + lists[i+2][j-2] + lists[i+3][j-3]) == 'MAS':
                    total += 1
                # check diagonally down right
                if (lists[i+1][j+1] + lists[i+2][j+2] + lists[i+3][j+3]) == 'MAS':
                    total += 1
    return total

# test
lists = read_file('test_data/day4.txt')
print("Test:", part1(lists))

# actual data
lists = read_file('data/day4.txt')
print("Actual:", part1(lists))

# Part 2
print("part 2")

# Similar to part 1 but instead of X, we are looking for A
# We need an A and an S in one diagnal and an A and an S in the other diagnal
def part2(lists):
    total = 0
    for i in range(3,(len(lists)-3)):
        for j in range(3,(len(lists[i])-3)):
            if lists[i][j] == 'A':
                double_mas = 0
                # Get top left, bottom right, top right, bottom left
                top_left = lists[i-1][j-1]
                bottom_right = lists[i+1][j+1]
                top_right = lists[i-1][j+1]
                bottom_left = lists[i+1][j-1]
                if top_left == 'S' and bottom_right == 'M' or top_left == 'M' and bottom_right == 'S':
                    double_mas += 1
                if top_right == 'S' and bottom_left == 'M' or top_right == 'M' and bottom_left == 'S':
                    double_mas += 1
                if double_mas == 2:
                    total += 1
    return total

# test
lists = read_file('test_data/day4.txt')
print("Test:", part2(lists))

# actual data
lists = read_file('data/day4.txt')
print("Actual:", part2(lists))
