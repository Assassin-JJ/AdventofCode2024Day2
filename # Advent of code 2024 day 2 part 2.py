# Advent of code 2024 day 2 part 2

def is_valid_sequence(numbers):
    if len(numbers) < 2:
        return False
    
    # Check first two numbers to determine direction
    increasing = numbers[1] > numbers[0]
    
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        
        # If increasing, diff should be positive and 1-3
        if increasing and (diff <= 0 or diff > 3):
            return False
        
        # If decreasing, diff should be negative and -1 to -3
        if not increasing and (diff >= 0 or diff < -3):
            return False
            
    return True

def check_sequence_with_removal(numbers):
    # First check if sequence is valid without removal
    if is_valid_sequence(numbers):
        return True
    
    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create new sequence without current number
        test_sequence = numbers[:i] + numbers[i+1:]
        if is_valid_sequence(test_sequence):
            return True
            
    return False

sequence_count = 0
with open('D:\Assorted_Scripts\AdventOfCode2024\AdventofCode2024Day2\Day2RawInput.txt', 'r') as file:
    for line in file:
        # Convert line to list of numbers
        numbers = [int(num) for num in line.strip().split()]
        
        # Check if sequence is valid or can be made valid
        if check_sequence_with_removal(numbers):
            sequence_count += 1

print(f"Number of valid sequences: {sequence_count}")