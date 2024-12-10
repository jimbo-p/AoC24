# read in data 
# it should be read into a dictionary with the kay as the number before the colon and the value as a list of the numbers after the colon
# each key / value pair corresponds to a row

def read_file(file_name):
    result = {}
    with open(file_name, 'r') as file:
        for line in file:
            # Split the line at the colon
            key, values = line.strip().split(':')
            # Convert the key to int and values to list of integers
            key = int(key)
            values = [int(x) for x in values.strip().split()]
            result[key] = values
    return result


# 11871769086942 too low
# 12553187649483 too low

# add to where I can see what is ruled bad and try to find edge case that is wrong
def check_validity(data):
    good_keys = []
    bad_data_copy = data.copy()
    for key, values in data.items():
        row_dict = {key: values}

        while True:
            if len(row_dict) == 0:
                break

            new_dict = {}
            #print("")
            for k, v in row_dict.items():
                #print("Keys: ", k, " Values: ", v)

                # stopping conditions
                if len(v) == 1:
                    if k == v[0]:
                        good_keys.append(key)
                        bad_data_copy.pop(key)
                        #print("Valid key found!: ", k, " with ", v, " original key ", key)
                        break
                    else:
                        continue

                # if k is divisible by the last value in v, need to check for both new keys
                if k % v[-1] == 0:
                    new_dict[k // v[-1]] = v[:-1]
                new_dict[k - v[-1]] = v[:-1]
            
            row_dict = new_dict
    return sum(good_keys), bad_data_copy
            
# Test Data
data = read_file('test_data/day7.txt')
answer, bad_data = check_validity(data)
print("Answer: ", answer)
for key, values in bad_data.items():
    print("Key: ", key, " Values: ", values)

# Real Data
data = read_file('data/day7.txt')
answer, bad_data = check_validity(data)
print("Answer: ", answer)
for key, values in bad_data.items():
    print("Key: ", key, " Values: ", values)
