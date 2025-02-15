# Function to calculate the average of a list
def Avg(numbers):
    total = 0
    count = 0  
    
    for number in numbers:
        total += number
        count += 1  # Counting elements manually

    return total / count  # Calculate and return average

# Function to calculate the sum of squared differences from the mean
def sumSqDiff(numbers):
    mean = Avg(numbers)  # Get the average
    total_squared_difference = 0
    
    for number in numbers:
        squared_difference = (number - mean) ** 2
        total_squared_difference += squared_difference  # Summing squared differences

    return total_squared_difference

# Main program for input 
print("Enter numbers separated by spaces: ")
user_input = input()  # Get user input
user_numbers = []  # Create an empty list