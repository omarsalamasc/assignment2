import random

# Generate a random temperature between 1 and 400
temper = random.randint(1, 400)

print("Temperature:", temper)

# Define temperature values
boilingPoint = 100
smokePoint = 320

# Check the temperature conditions using nested if-else
if temper > boilingPoint:
    if temper > smokePoint:
        print("Temperature above smoke point")
    else:
        print("Temperature above boiling point")
else:
    print("Temperature is not very high")