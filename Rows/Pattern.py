# Get user input for number of rows
rows = int(input("Enter the number of rows: "))

# Loop to generate pattern
for i in range(1, rows + 1):
    if i % 2 == 1:  # Odd row
        print("+" * i)
    else:  # Even row
        print("-" * i)