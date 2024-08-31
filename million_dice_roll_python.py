"""
    Filename: million_dice_roll_python.py
    Created: 06/12/22
    Adapted from: Million Dice Roll Statistics Simulator
    By Al Sweigart www.inventwithpython.com
    Purpose: A simulation of one million dice rolls
"""
import random
import time
# 1,000,000 rolls
NUMBER_OF_DICE_ROLLS = 1000000
print(" +----------------------------------------------+")
print(" |--  Million Dice Roll Statistics Simulator  --|")
print(" +----------------------------------------------+")

number_of_dice = int(
    input(" How many 6 sided dice do you want to roll?\n (min=2): "))
# Do not allow less than 2 dice
if number_of_dice < 2:
    number_of_dice = 2

# Set up a dictionary to store the results of all dice rolls
results = {}
# Fill dictionary keys with all possible combinations of dice
# Example: 2 dice: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
# Initialize the values to 0
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

print(f" Simulating 1,000,000 rolls of {number_of_dice} dice...")

# Record calculation start time
start_time = time.time()

# Roll the number_of_dice dice 1,000,000 times
for i in range(NUMBER_OF_DICE_ROLLS):
    total = 0
    for j in range(0, number_of_dice):
        # Accumulate Sum of all dice rolls of number_of_dice
        total = total + random.randint(1, 6)
    # Add 1 to the appropriate result dictionary key
    results[total] = results[total] + 1

# Record calculation finish time
finish_time = time.time()
# Calculate elapsed time in ms (milliseconds)
elapsed_time = finish_time - start_time
# Convert seconds to ms, 1000 ms in a second
elapsed_time = elapsed_time * 1000
print(f" Elapsed time: {round(elapsed_time):,} ms")

# Display results
print(" Total  Rolls  Percentage")
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    # Calculate percentage rounded to 1 decimal place
    # Move decimal point over to show percentage
    percentage = round(roll / 10000, 1)
    print(f'{i:3} {roll:9,} {percentage:>6}%')
input("Press Enter to exit")
