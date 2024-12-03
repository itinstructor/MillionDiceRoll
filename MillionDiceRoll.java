
/**
 * Name: MillionDiceRoll.java
 * Written by:
 * Written on: 06/12/2022
 * Purpose: Roll dice 1,000,000 times
 */

// import java.text.DecimalFormat;
import java.util.*;
// Import java Random library
import java.util.Random;

public class MillionDiceRoll {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        // Format to show 1 decimal place
        // DecimalFormat df = new DecimalFormat("#.0");
        // DecimalFormat if = new DecimalFormat("###,###,###");
        Random random = new Random();
        final int MIN = 1;
        final int MAX = 6;
        int numberOfDice = 0;

        // Create a HashTable key value pair dictionary
        Hashtable<Integer, Integer> myDict = new Hashtable<Integer, Integer>();
        System.out.println(" +-------------------------------------------+");
        System.out.println(" |--  Million Dice Roll Statics Simulator  --|");
        System.out.println(" +-------------------------------------------+");
        System.out.print(" How many dice do you want to roll?\n (min=2): ");

        numberOfDice = Integer.parseInt(keyboard.nextLine());

        if (numberOfDice < 2) {
            numberOfDice = 2;
        }

        // Fill dictionary keys with possible combinations of dice
        // Initialize the values to 0
        for (int i = numberOfDice; i < (numberOfDice * 6) + 1; i++) {
            myDict.put(i, 0);
        }

        System.out.println(" Simulating 1,000,000 rolls of " + numberOfDice + " dice...");

        // Record start calculation time
        // On a 64 bit sytem, long is 64 bits in size while int is 32 bits
        long start = System.currentTimeMillis();

        // Roll dice 1,000,000 times
        for (int i = 0; i < 1000000; i++) {
            int total = 0;
            for (int j = 0; j < numberOfDice; j++) {

                // Generate random number between
                // MIN and MAX inclusive, accumulate to total for each dice
                total = total + random.nextInt(MIN, MAX + 1);
            }
            // Add one to the total key to increment the number of times
            // the dice added up to that number
            myDict.put(total, myDict.get(total) + 1);
        }

        // Record finish calculation time
        long finish = System.currentTimeMillis();

        // Calculate elapsed time
        long timeElapsed = finish - start;
        // Display elapsed time in ms
        System.out.println(" Elapsed time: " + timeElapsed + " ms");

        // Print result heading
        System.out.println(" Total - Rolls - Percent");
        // Display roll statistics
        for (int i = numberOfDice; i < (numberOfDice * 6); i++) {
            int rolls = myDict.get(i);
            // Calculate percentage rounded to 1 decimal place
            double percentage = Math.round((rolls * 10.0) / 10000.0) / 10.0;
            // Display results
            System.out.printf(" %-4d %,7d %7.1f%s\n", i, rolls, percentage, "%");
        }
        keyboard.close();
    }
}
