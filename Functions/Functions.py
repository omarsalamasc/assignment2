# Function to calculate the average of a list
def avg(numbers):
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

# Function to calculate the sum of squared differences from the mean
def sum_sq_diff(numbers):
    mean = avg(numbers)  # Get the average
    total_squared_difference = 0
    
    for number in numbers:
        squared_difference = (number - mean) ** 2
        total_squared_difference += squared_difference

    return total_squared_difference

# Main program for input 
print("Enter numbers separated by spaces: ")
user_input = input()  # Get user input
user_numbers = []

