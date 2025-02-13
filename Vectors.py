# creating an empty list to store vector components
dimensions = ['x', 'y', 'z']
vector = [0, 0, 0]

# Get user input using a for loop
for i in range(3):
    vector[i] = int(input("Enter value for " + dimensions[i] + ": "))
    print(i)

# Calculate sum of squares using a for loop
sum_of_squares = 0
for i in range(3):
    sum_of_squares = sum_of_squares + (vector[i] * vector[i])
    print("Current sum of squares:", sum_of_squares)