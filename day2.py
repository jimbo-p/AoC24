# Get data from text file and generate many lists
# Each row of text should be a list of numbers
# A list of the lists shoudl be returned
def generate_lists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lists = []
    for line in lines:
        lists.append(list(map(int, line.split())))

    return lists

# Part 1
print("Part 1")

# Two  rules to incorporate
# 1. The list of numbers should be decreasing or increasing
# 2. Each sequential number must increase / decrease by at least 1 and at most 3

def is_decreasing(l: list[int]):
    return all(l[i] >= l[i+1] for i in range(len(l) - 1))

def is_increasing(l: list[int]):
    return all(l[i] <= l[i+1] for i in range(len(l) - 1))

def numbers_within_range(l: list[int]):
    return all(abs(l[i] - l[i+1]) >= 1 and abs(l[i] - l[i+1]) <= 3 for i in range(len(l) - 1))

def solve_part_1(lists: list[list[int]]):
    total_valid_reports = 0
    for list in lists:
        if (is_decreasing(list) or is_increasing(list)) and numbers_within_range(list):
            total_valid_reports += 1
    return total_valid_reports

# test data
lists = generate_lists('test_data/day2.txt')
print("Test result:", solve_part_1(lists))

# actual data
lists = generate_lists('data/day2.txt')
print("Actual result:", solve_part_1(lists))


# Part 2
print("Part 2")
# One additional rule to incorporate
# In a given list, a single number can be removed and then the solution can be tested
# We will need to repeat part 1 but for any list which isn't safe, loop through each number and remove it and then test the solution
# If a safe solution is found by removing a number, make it as valid and move to then next list

def is_safe(l: list[int]):
    return (is_decreasing(l) or is_increasing(l)) and numbers_within_range(l)

def solve_part_2(lists: list[list[int]]):
    total_valid_reports = 0
    for list in lists:
        if not is_safe(list):
            for i in range(len(list)):
                if is_safe(list[:i] + list[i+1:]):
                    total_valid_reports += 1
                    break
        else:
            total_valid_reports += 1
    return total_valid_reports


# test data
lists = generate_lists('test_data/day2.txt')
print("Test result:", solve_part_2(lists))

# actual data
lists = generate_lists('data/day2.txt')
print("Actual result:", solve_part_2(lists))






