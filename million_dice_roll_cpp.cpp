/**
 * Name: million_dice_roll_cpp.cpp
 * Written by:
 * Written on:
 * Purpose: Roll dice 1,000,000 times
 */
#include <iostream>
#include <unordered_map>
#include <cmath>
#include <chrono>
#include <locale.h>
#include <cstdlib>
int main()
{
    const int MIN{1};
    const int MAX{6};
    int numberOfDice{0};
    // Seed random number with random time
    srand(time(0));
    // Create a unordered_map HashTable key value pair dictionary
    std::unordered_map<int, int> myDict;
    std::cout << " +-------------------------------------------+" << std::endl;
    std::cout << " |--  Million Dice Roll Statics Simulator  --|" << std::endl;
    std::cout << " +-------------------------------------------+" << std::endl;
    std::cout << " How many dice do you want to roll? \n (min=2): ";

    std::cin >> numberOfDice;
    if (numberOfDice < 2)
    {
        numberOfDice = 2;
    }

    // Fill unordered_map (dictionary) keys with possible combinations of dice
    // Initialize the values to 0
    for (int i = numberOfDice; i < (numberOfDice * 6) + 1; i++)
    {
        myDict[i] = 0;
    }

    std::cout << "\n Simulating 1,000,000 rolls of "
              << numberOfDice << " dice..." << std::endl;
    // Begin calculation time
    std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();

    for (int i = 0; i < 1000000; i++)
    {
        int total = 0;
        for (int j = 0; j < numberOfDice; j++)
        {
            // Generate random number between MIN and MAX inclusive,
            // Accumulate to total for each dice
            total = total + rand() % MAX + MIN;
        }
        // Add one to the total key to increment the number of times
        // the dice added up to that number
        myDict[total] = myDict[total] + 1;
    }
    // Finish calculation time
    std::chrono::steady_clock::time_point finish = std::chrono::steady_clock::now();
    // On a 64 bit sytem, long is 64 bits in size while int is 32 bits
    long elapsedTime = std::chrono::duration_cast<std::chrono::milliseconds>(finish - start).count();
    // Calculate and display elapsed time in ms
    std::cout << " Elapsed time: " << elapsedTime << "ms" << std::endl;

    // Print result heading
    std::cout << " Total - Rolls - Percent" << std::endl;
    for (int i = numberOfDice; i < numberOfDice * 6; i++)
    {
        int rolls = myDict[i];
        // Round to one decimal places
        double percentage = round((rolls * 100) / 10000.0) / 100.0;
        // std::cout << "  " << i << " - " << rolls << " - " << percentage << "%" << std::endl;
        // Used to set commas in int rolls with '
        setlocale(LC_NUMERIC, "");
        // Formatting: % is the placeholder for the variable
        // -4d aligns integers to the left at 4 spaces
        // '7d aligns integers to the right at 7 spaces ' puts in a thousands separator
        // 7.1f aligns floats to the right at 7 spaces
        // s inserts the string "%"
        // \n inserts a new line
        printf("  %-4d %'7d %7.1f%s\n", i, rolls, percentage, "%");
    }

    // Pause program before exit
    system("pause");
    return 0;
}
