# Get user input for number of rows
rows = int(input("Enter the number of rows: "))

# Loop to generate pattern
for i in range(1, rows + 1):
    if i % 2 == 1:  # Odd row
        print("+" * i)
    else:  # Even row
        print("-" * i)

# Initialize list with 10 scores
scores = [85, 72, 90, 66, 45, 78, 58, 92, 81, 49]

# Loop through scores and assign grades
for score in scores:
    if score > 80:
        grade = "A"
    elif score > 70:
        grade = "B"
    elif score > 60:
        grade = "C"
    elif score > 50:
        grade = "D"
    else:
        grade = "F"
    
    print("Score: " + score, "Grade: " + grade)