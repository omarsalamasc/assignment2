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

# calculating square root using a for loop
print("Computing square root approximation:")
approx = sum_of_squares  # Initial guess
for i in range(10):  # Approximate square root using 10 iterations
    approx = (approx + sum_of_squares / approx) / 2
    print("Iteration", i + 1, "approximate square root:", approx)

# Display the result
print("The magnitude of the vector is:", approx)