# Advent of code 2024 day 2 part 1

def check_sequence(numbers):
    if len(numbers) < 2:
        return False
    
    # Check first two numbers to determine if sequence should increase or decrease
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

sequence_count = 0
with open('D:\Assorted_Scripts\AdventOfCode2024\AdventofCode2024Day2\Day2RawInput.txt', 'r') as file:
    for line in file:
        # Convert line to list of numbers
        numbers = [int(num) for num in line.strip().split()]
        
        # Check if sequence follows the rules
        if check_sequence(numbers):
            sequence_count += 1

print(f"Number of valid sequences: {sequence_count}")
