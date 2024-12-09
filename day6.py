# Read in the data from a text file
# Each row is a string that should be made into a list of characters. 

def read_file(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    # pad data with "x" on top / bottom
    data = ['x' * (len(data[0]) + 1)] + ['x' + row.strip() + 'x' for row in data] + ['x' * (len(data[0]) + 1)]
    return [list(row) for row in data]


# Get Starting position (where the ^ is)
def get_start(data):
    for row in data:
        if '^' in row:
            start_row = data.index(row)
            start_col = row.index('^')
            break
    return start_row, start_col


# Part 1
print("Part 1")

# initialize a grid of all zeros, the same size as the data
def initialize_grid(data):
    grid = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
    return grid

def path_traveled(data, grid, start_row, start_col):
    direction = 'up'
    while True:
        if direction == 'up':
            if data[start_row - 1][start_col] == '#':
                direction = 'right'
                continue
            elif data[start_row - 1][start_col] == 'x':
                break
            else:
                start_row -= 1
                grid[start_row][start_col] = 1
                continue
        elif direction == 'right':
            if data[start_row][start_col + 1] == '#':
                direction = 'down'
                continue
            elif data[start_row][start_col + 1] == 'x':
                break
            else:
                start_col += 1
                grid[start_row][start_col] = 1
                continue
        elif direction == 'down':
            if data[start_row + 1][start_col] == '#':
                direction = 'left'
                continue
            elif data[start_row + 1][start_col] == 'x':
                break
            else:
                start_row += 1
                grid[start_row][start_col] = 1
                continue
        elif direction == 'left':
            if data[start_row][start_col - 1] == '#':
                direction = 'up'
                continue
            elif data[start_row][start_col - 1] == 'x':
                break
            else:
                start_col -= 1
                grid[start_row][start_col] = 1
                continue

    return grid

# Test
data = read_file('test_data/day6.txt')
start_row, start_col = get_start(data)
grid = initialize_grid(data)
grid[start_row][start_col] = 1
grid = path_traveled(data, grid, start_row, start_col)

total = 0
for g in grid:
    total += sum(g)

print("Test: ", total)

# Actual
data = read_file('data/day6.txt')
start_row, start_col = get_start(data)
grid = initialize_grid(data)
grid[start_row][start_col] = 1
grid = path_traveled(data, grid, start_row, start_col)

total = 0
for g in grid:
    total += sum(g)

print("Actual: ", total)

# Part 2
print("Part 2")

def loop_check(data, start_row, start_col):
    direction = 'up'
    num_steps = 0
    
    while True:
        num_steps += 1
        if num_steps > 10000:
            return True
        if direction == 'up':
            if data[start_row - 1][start_col] == '#':
                direction = 'right'
                continue
            elif data[start_row - 1][start_col] == 'x':
                break
            else:
                start_row -= 1
                continue
        elif direction == 'right':
            if data[start_row][start_col + 1] == '#':
                direction = 'down'
                continue
            elif data[start_row][start_col + 1] == 'x':
                break
            else:
                start_col += 1
                continue
        elif direction == 'down':
            if data[start_row + 1][start_col] == '#':
                direction = 'left'
                continue
            elif data[start_row + 1][start_col] == 'x':
                break
            else:
                start_row += 1
                continue
        elif direction == 'left':
            if data[start_row][start_col - 1] == '#':
                direction = 'up'
                continue
            elif data[start_row][start_col - 1] == 'x':
                break
            else:
                start_col -= 1
                continue

    return False

# Determine where to place the obstancle based on the grid from part 1
def place_obstacle(data, grid, start_row, start_col):
    loop_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and not (row == start_row and col == start_col):
                data[row][col] = '#'
                if loop_check(data, start_row, start_col):
                    loop_count += 1
                data[row][col] = '.'

    return loop_count

# Test
data = read_file('test_data/day6.txt')
start_row, start_col = get_start(data)
grid = initialize_grid(data)
grid[start_row][start_col] = 1
grid = path_traveled(data, grid, start_row, start_col)
print(place_obstacle(data, grid, start_row, start_col))

# Actual
data = read_file('data/day6.txt')
start_row, start_col = get_start(data)
grid = initialize_grid(data)
grid[start_row][start_col] = 1
grid = path_traveled(data, grid, start_row, start_col)
print(place_obstacle(data, grid, start_row, start_col))

    


