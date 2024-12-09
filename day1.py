# Take a text file with two numbers per row and generate two lists, one with the first number and one with the second number.
def generate_lists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    first_numbers = []
    second_numbers = []

    for line in lines:
        first, second = map(int, line.split())
        first_numbers.append(first)
        second_numbers.append(second)

    return first_numbers, second_numbers

# Part 1
def calculate_total_distance(first_numbers, second_numbers):
    # Sort the numbers in the lists
    first_numbers.sort()
    second_numbers.sort()

    # Get the distance between the first and second numbers
    distances = [abs(first - second) for first, second in zip(first_numbers, second_numbers)]

    # Get the sum of the distances and ensure it is positive
    return sum(distances)

print("Part 1")
# Test run
first_numbers, second_numbers = generate_lists('test_data/day1.txt')
result = calculate_total_distance(first_numbers, second_numbers)
print("Test result:", result)

# Run with actual data
first_numbers, second_numbers = generate_lists('data/day1.txt')
result = calculate_total_distance(first_numbers, second_numbers)
print("Actual result:", result)

# Part 2
print("Part 2") 
# Find number of times number from first list appears in the second list
# Store the result in a dictionary with the number as the key and the count as the value

occurrences = {}
def solve_part_2(first_numbers, second_numbers):
    for first in first_numbers:
        occurrences[first] = sum(1 for second in second_numbers if first == second)
    
    total = 0
    for number in first_numbers:
        total += number * occurrences[number]

    return total


# Test run
first_numbers, second_numbers = generate_lists('test_data/day1.txt')
result = solve_part_2(first_numbers, second_numbers)
print("Test result:", result)

# Run with actual data
first_numbers, second_numbers = generate_lists('data/day1.txt')
result = solve_part_2(first_numbers, second_numbers)
print("Actual result:", result)
