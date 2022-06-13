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

            Console.WriteLine(" +-------------------------------------------+");
            Console.WriteLine(" |--  Million Dice Roll Statics Simulator  --|");
            Console.WriteLine(" +-------------------------------------------+");
            Console.Write(" How many dice do you want to roll: ");

            int numberOfDice = Convert.ToInt32(Console.ReadLine());

            for (int i = numberOfDice; i < (numberOfDice * 6) + 1 ; i++)
            {
                myDict.Add(i, 0);
            }
            Console.WriteLine(" Simulating 1,000,000 rolls of " + numberOfDice + " dice...");

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
            Console.WriteLine(" Total  Rolls  Percent");
            for (int i = 2; i < 13; i++)
            {
                int rolls = myDict[i];
                double percentage = Math.Round(rolls / 10000.0);
                Console.WriteLine($" {i, 2} {rolls, 9:n0} {percentage, 6:n1}%");
            }
            // Pause execution
            Console.WriteLine("\nPress Enter to exit");
            Console.ReadLine();
        }
    }
}
