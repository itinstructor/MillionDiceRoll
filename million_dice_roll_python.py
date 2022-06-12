"""
    Filename: million_dice_roll.py
    Adapted from: Million Dice Roll Statistics Simulator
    By Al Sweigart www.inventwithpython.com
    A simulation of one million dice rolls.
"""
import random
import time

print("Million Dice Roll Statistics Simulator")

number_of_dice = int(input("Enter how many six-sided dice you want to roll: "))

# Set up a dictionary to store the results of each dice roll:
results = {}
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

print(f'Simulating 1,000,000 rolls of {number_of_dice} dice...')

# Start calculation time
start = time.time()
for i in range(1000000):
    total = 0
    for j in range(number_of_dice):
        # total is the sum of all dice rolls
        total = total + random.randint(1, 6)
    # Add 1 to the result dictionary key
    results[total] = results[total] + 1

# End calculation time
finish = time.time()
# Calculate and display elapsed time in seconds
elapsed_time = finish - start
# Convert seconds to ms (milliseconds)
elapsed_time = elapsed_time * 1000
print(f"Elapsed time: {round(elapsed_time)} ms")

# Display results
print('TOTAL - ROLLS - PERCENTAGE')
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print(f'  {i} - {roll} - {percentage}%')
