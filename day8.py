# Read in data from file

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data

# Each line should be a list of characters
def parse_data(data):
    return [list(line.strip()) for line in data]

# Create a dict which maps each character to its position
# ignore "."
def create_dict(data):
    char_dict = {}
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                if char not in char_dict:
                    char_dict[char] = []
                char_dict[char].append((i, j))
    return char_dict

# Part 1
def part1(data):
    data = parse_data(data)
    char_dict = create_dict(data)
    antinode_locations = []
    unique_antinode_locations = 0

    # create map to visualize the antinodes
    antinode_map = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    
    for k, v in char_dict.items():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                x_dist = v[i][0] - v[j][0]
                y_dist = v[i][1] - v[j][1]

                p1 = (v[i][0] + x_dist, v[i][1] + y_dist)
                p2 = (v[j][0] - x_dist, v[j][1] - y_dist)

                # Only update map and count if points are in bounds
                if p1[0] >= 0 and p1[1] >= 0 and p1[0] < len(data) and p1[1] < len(data[0]):
                    antinode_locations.append(p1)
                    antinode_map[p1[0]][p1[1]] = 1

                if p2[0] >= 0 and p2[1] >= 0 and p2[0] < len(data) and p2[1] < len(data[0]):
                    antinode_locations.append(p2)
                    antinode_map[p2[0]][p2[1]] = 1

    unique_antinode_locations = len(set(antinode_locations))
    
    #for row in antinode_map:
        # print row as a string
    #    print(''.join(str(x) for x in row))
    return unique_antinode_locations



# Test Data
data = read_file('test_data/day8.txt')
print(part1(data))

# Actual Data
data = read_file('data/day8.txt')
print(part1(data))

# Part 2
def part2(data):
    data = parse_data(data)
    char_dict = create_dict(data)
    antinode_locations = []
    unique_antinode_locations = 0

    # create map to visualize the antinodes
    antinode_map = [["." for _ in range(len(data[0]))] for _ in range(len(data))]
    
    for k, v in char_dict.items():
        if len(v) > 1:
            for loc in v:
                antinode_locations.append(loc)
                antinode_map[loc[0]][loc[1]] = 1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                x_dist = v[i][0] - v[j][0]
                y_dist = v[i][1] - v[j][1]

                p1 = (v[i][0] + x_dist, v[i][1] + y_dist)
                p2 = (v[j][0] - x_dist, v[j][1] - y_dist)

                while p1[0] >= 0 and p1[1] >= 0 and p1[0] < len(data) and p1[1] < len(data[0]):
                    antinode_locations.append(p1)
                    antinode_map[p1[0]][p1[1]] = 1
                    p1 = (p1[0] + x_dist, p1[1] + y_dist)

                while p2[0] >= 0 and p2[1] >= 0 and p2[0] < len(data) and p2[1] < len(data[0]):
                    antinode_locations.append(p2)
                    antinode_map[p2[0]][p2[1]] = 1
                    p2 = (p2[0] - x_dist, p2[1] - y_dist)

    unique_antinode_locations += len(set(antinode_locations))
    
    #for row in antinode_map:
        # print row as a string
    #    print(''.join(str(x) for x in row))


    return unique_antinode_locations

# Test Data
data = read_file('test_data/day8.txt')
print(part2(data))

# Actual Data
data = read_file('data/day8.txt')
print(part2(data))

