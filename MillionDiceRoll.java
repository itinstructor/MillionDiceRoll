
/**
 * Name: MillionDiceRoll.java
 * Written by:
 * Written on:
 * Purpose: Roll dice 1,000,000 times
 */

import java.util.*;
// Import library for random numbers
import java.util.concurrent.ThreadLocalRandom;

public class MillionDiceRoll {
    public static void main(String[] args) {
        final int MIN = 1;
        final int MAX = 6;
        // Create a HashTable key value pair dictionary
        Hashtable<Integer, Integer> myDict = new Hashtable<Integer, Integer>();

        for (int i = 2; i < 13; i++) {
            myDict.put(i, 0);
        }
        System.out.println("\nSimulating 1,000,000 rolls of 2 dice...");

        // Record start calculation time
        // On a 64 bit sytem, long is 64 bits in size while int is 32 bits
        long start = System.nanoTime();

        // Roll dice 1,000,000 times
        for (int i = 0; i < 1000000; i++) {
            int total = 0;
            for (int j = 0; j < 2; j++) {

                // Generate random number between
                // MIN and MAX inclusive, accumulate to total for each dice
                total = total + ThreadLocalRandom.current().nextInt(MIN, MAX + 1);
            }
            // Add one to the total key to increment the number of times
            // the dice added up to that number
            myDict.put(total, myDict.get(total) + 1);
        }

        // Record finish calculation time
        long finish = System.nanoTime();

        // Calculate elapsed time
        long timeElapsed = finish - start;
        // Display elapsed time in ms
        System.out.println("Elapsed time: " + timeElapsed / 1000000 + " ms");

        // Print result heading
        System.out.println("Total - Rolls - Percent");
        for (int i = 2; i < 13; i++) {
            int rolls = myDict.get(i);
            double percentage = Math.round(rolls / 10000.0);
            System.out.println(i + "       " + rolls + "   " + percentage + "%");
        }
    }
}
