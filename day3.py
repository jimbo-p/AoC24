import re

# Read in the text file as one continuous string. 
# Make it generic in which file it is read from.
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Part 1
print("Part 1")

# Looking to do some regext to find valid expressions within the string
# The regex should be able to find the following:
# Sequence must start with "mul("
# "mul(" must be followed by two numbers separated by a comma
# After the last of the two numbers, there must be a closing parenthesis

def find_mul_expressions(text):
    # The regex pattern to find the valid expressions
    pattern = r'mul\(([0-9]+),([0-9]+)\)'
    return re.findall(pattern, text)

def convert_mul_expressions(l: list):
    total = 0
    for t in l:
        total += int(t[0]) * int(t[1])
    return total

# Test the function with the provided text
# test
text = read_file('test_data/day3.txt')
print(convert_mul_expressions(find_mul_expressions(text)))

# data  
text = read_file('data/day3.txt')
print(convert_mul_expressions(find_mul_expressions(text)))

print("Part 2")

# The original string needs to be edited.
# Within the string, there are some "do()" and "don't()" instructions
# We want to remove anything between a "don't()" and the next "do()"

def remove_dont_do_instructions(text):
    result = []
    i = 0
    while i < len(text):
        if text[i:i+6] == "don't(":
            # Skip past "don't()"
            i += 6
            # Skip characters until "do()" is found
            while i < len(text) and text[i:i+3] != "do(":
                i += 1
        elif text[i:i+3] == "do(":
            # Append "do()" to the result
            result.append("do()")
            # Skip past "do()"
            i += 3
        else:
            # Append current character to the result
            result.append(text[i])
            i += 1
    return ''.join(result)

text = read_file('test_data/day3.txt')
text = remove_dont_do_instructions(text)
print(convert_mul_expressions(find_mul_expressions(text)))

text = read_file('data/day3.txt')
text = remove_dont_do_instructions(text)
print(convert_mul_expressions(find_mul_expressions(text)))

