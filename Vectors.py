# creating an empty list to store vector components
dimensions = ['x', 'y', 'z']
vector = [0, 0, 0]

# Get user input using a for loop
for i in range(3):
    vector[i] = int(input("Enter value for " + dimensions[i] + ": "))
    print(i)
