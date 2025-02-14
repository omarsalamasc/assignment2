# Initialize variables
count = 0

# While loop to take user input until a negative number is entered
print("Enter numbers (enter a negative number to stop):")

while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        break  # Exit loop if the user enters a negative number
    
    print("You entered:", num)
    count += 1  # Increment count

# Display the number of iterations
print("The loop ran", count, "times.")