/**
 * Name: million_dice_roll.cpp
 * Written by:
 * Written on:
 * Purpose: Roll dice 1,000,000 times
 */
#include <iostream>
#include <unordered_map>
#include <cmath>
#include <chrono>
int main()
{
    const int MIN = 1;
    const int MAX = 6;
    // Seed random number
    srand(time(0));
    // Create a unordered_map HashTable key value pair dictionary
    std::unordered_map<int, int> myDict;

    for (int i = 2; i < 13; i++)
    {
        myDict[i] = 0;
    }

    std::cout << "\nSimulating 1,000,000 rolls of 2 dice..." << std::endl;
    // Begin calculation time
    std::chrono::steady_clock::time_point start = std::chrono::steady_clock::now();

    for (int i = 0; i < 1000000; i++)
    {
        int total = 0;
        for (int j = 0; j < 2; j++)
        {
            // Generate random number between MIN and MAX inclusive,
            // Accumulate to total for each dice
            total = total + rand() % MAX + MIN;
        }
        // Add one to the total key to increment the number of times
        // the dice added up to that number
        // myDict.put(total, myDict.get(total) + 1);
        myDict[total] = myDict[total] + 1;
    }
    // Finish calculation time
    std::chrono::steady_clock::time_point finish = std::chrono::steady_clock::now();
    // On a 64 bit sytem, long is 64 bits in size while int is 32 bits
    long elapsedTime = std::chrono::duration_cast<std::chrono::milliseconds>(finish - start).count();
    // Calculate and display elapsed time in ms
    std::cout << "Elapsed time: " << elapsedTime << "ms" << std::endl;

    // Print result heading
    std::cout << "Total - Rolls - Percent" << std::endl;
    for (int i = 2; i < 13; i++)
    {
        int rolls = myDict[i];
        // Round to two decimal places
        double percentage = round((rolls * 100) / 10000.0) / 100.0;
        std::cout << "  " << i << " - " << rolls << " - " << percentage << "%" << std::endl;
    }
    return 0;
}
