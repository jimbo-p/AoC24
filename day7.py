from collections import defaultdict

# read in data 
# it should be read into a dictionary with the kay as the number before the colon and the value as a list of the numbers after the colon
# each key / value pair corresponds to a row

def read_file(file_name):
    keys = []
    all_values = []
    
    with open(file_name, 'r') as file:
        for line in file:
            key, values = line.strip().split(':')
            # Convert key to int and add to keys list
            keys.append(int(key))
            # Convert values to list of integers and add to values list
            values = [int(x) for x in values.strip().split()]
            all_values.append(values)
    
    return keys, all_values


# 11871769086942 too low
# 12553187649483 too low
# 12553187650171

# add to where I can see what is ruled bad and try to find edge case that is wrong
def check_validity_p1(keys, values):
    good_keys = []
    for i in range(len(keys)):
        possible_values = [values[i].pop(0)]
        remaining_values = values[i].copy()
        
        while remaining_values:
            v = remaining_values.pop(0)
            temp = []
            for p in possible_values:
                temp.append(p + v)
                temp.append(p * v)
            possible_values = temp

        if keys[i] in possible_values:
            good_keys.append(keys[i])

    return sum(good_keys)

# Test Data
keys, values = read_file('test_data/day7.txt')
answer = check_validity_p1(keys, values)
print("Answer: ", answer)

# Real Data
keys, values = read_file('data/day7.txt')
answer = check_validity_p1(keys, values)
print("Answer: ", answer)

def check_validity_p2(keys, values):
    good_keys = []
    for i in range(len(keys)):
        possible_values = [values[i].pop(0)]
        remaining_values = values[i].copy()
        
        while remaining_values:
            v = remaining_values.pop(0)
            temp = []
            for p in possible_values:
                temp.append(p + v)
                temp.append(p * v)
                temp.append(int(str(p) + str(v)))
            possible_values = temp

        if keys[i] in possible_values:
            good_keys.append(keys[i])

    return sum(good_keys)

# Test Data
keys, values = read_file('test_data/day7.txt')
answer = check_validity_p2(keys, values)
print("Answer: ", answer)

# Real Data
keys, values = read_file('data/day7.txt')
answer = check_validity_p2(keys, values)
print("Answer: ", answer)

