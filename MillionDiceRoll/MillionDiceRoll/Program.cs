using System;
using System.Collections.Generic;

namespace MillionDiceRoll
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Random randInt = new Random();
            DateTime startTime, finishTime;
            const int MIN = 1;
            const int MAX = 6;
            // Create a HashTable key value pair dictionary
            Dictionary<int, int> myDict = new Dictionary<int, int>();

            for (int i = 2; i < 13; i++)
            {
                myDict.Add(i, 0);
            }
            Console.WriteLine("\nSimulating 1,000,000 rolls of 2 dice...");

            // Record start calculation time
            startTime = DateTime.Now;

            // Roll dice 1,000,000 times
            for (int i = 0; i < 1000000; i++)
            {
                int total = 0;
                for (int j = 0; j < 2; j++)
                {
                    // Generate random number between
                    // MIN and MAX inclusive, accumulate to total for each dice
                    total = total + randInt.Next(MIN, MAX + 1);
                }
                // Add one to the total key to increment the number of times
                // the dice added up to that number
                myDict[total] = myDict[total] + 1;
            }

            // Record finish calculation time
            finishTime = DateTime.Now;

            // Calculate elapsed time
            double elapsedTime = ((TimeSpan)(finishTime - startTime)).TotalMilliseconds;
            // Display elapsed time in ms
            Console.WriteLine("Elapsed time: " + Math.Round(elapsedTime) + " ms");

            // Print result heading
            Console.WriteLine("Total - Rolls - Percent");
            for (int i = 2; i < 13; i++)
            {
                int rolls = myDict[i];
                double percentage = Math.Round(rolls / 10000.0);
                Console.WriteLine("  "+ i + " - " + rolls + " - " + percentage + "%");
            }
            // Pause execution
            Console.ReadLine();
        }
    }
}
