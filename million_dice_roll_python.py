"""
    Filename: million_dice_roll.py
    Created: 06/12/22
    Adapted from: Million Dice Roll Statistics Simulator
    By Al Sweigart www.inventwithpython.com
    Purpose: A simulation of one million dice rolls
"""
import random
import time
print(" +--------------------------------------------+")
print(" |-- Million Dice Roll Statistics Simulator --|")
print(" +--------------------------------------------+")

number_of_dice = int(input(" How many dice do you want to roll: "))

# Set up a dictionary to store the results of each dice roll
results = {}
# Fill dictionary keys with possible combinations of dice
# Initialize the values to 0
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

print(f" Simulating 1,000,000 rolls of {number_of_dice} dice...")

# Record start calculation time
start_time = time.time()

# Roll the dice 1,000,000 times
for i in range(1000000):
    total = 0
    for j in range(number_of_dice):
        # total is the sum of all dice rolls of number_of_dice
        total = total + random.randint(1, 6)
    # Add 1 to the appropriate result dictionary key
    results[total] = results[total] + 1

# Record finish calculation time
finish_time = time.time()
# Calculate and display elapsed time in ms (milliseconds)
elapsed_time = finish_time - start_time
# Convert seconds to ms
elapsed_time = elapsed_time * 1000
print(f" Elapsed time: {round(elapsed_time)} ms")

# Display results
print(" Total  Rolls  Percentage")
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'{i:3} {roll:10,} {percentage:>6}%')
