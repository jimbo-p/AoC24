# Generate two lists from a .txt file
# The first list consists of a list of tuples. The tuples are made from each line with a "|" between the two numbers
# The second list can be found with a page break in the file.
# The second list is a list of lists. Each list is a list of numbers separated by commas. It should be made into a list of ints.

def read_file(file_name):
    # Read the first list
    first_list = []
    second_list = []
    with open(file_name, 'r') as file:
        for line in file:
            if '|' in line:
                first_list.append(tuple(map(int, line.split('|'))))
            
            if "," in line:
                second_list.append(list(map(int, line.split(','))))
            
    return first_list, second_list




# Part 1
print("Part 1")

def good_bad_check(rules, updates):
    good_updates = []
    bad_updates = []
    for update in updates:
        good = True
        for ind, number in enumerate(reversed(update)):
            if good == False:
                break
            for rule in rules:
                if number == rule[0] and rule[1] in update[:(len(update) - ind)]:
                    good = False
                    break
        if good:
            good_updates.append(update)
        else:
            bad_updates.append(update)
    return good_updates, bad_updates

def middle_value(good_lists):
    total = 0
    for good_list in good_lists:
        total += good_list[len(good_list) // 2]
    
    return total

# Test
rules, updates = read_file('test_data/day5.txt')
good, bad = good_bad_check(rules, updates)
print(good)
print("Test:", middle_value(good))

# Actual
# 5782 too high
rules, updates = read_file('data/day5.txt')
good, bad = good_bad_check(rules, updates)
print("Actual:", middle_value(good))



