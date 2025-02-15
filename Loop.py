# Initialize variables
count = 0
student_number = 991786467  # my student number

print("Enter numbers (enter a negative number to stop or student number):") 

while True:
    num = int(input("Enter a number: "))
    
    if num == student_number:
        print("cutoff point")  # Print message when student number is entered
        break  # Exit loop
    
    if num % 11 == 0:
        continue  # Skip current iteration if num is a multiple of 11
    
    print("You entered:", num)
    count += 1  # Increment count only if num is not a multiple of 11

# Display the number of valid iterations
print("The loop ran", count, "times.")