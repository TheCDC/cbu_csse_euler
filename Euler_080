/**
 * Created by Anthony Henson on 2/8/2017.
 */

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;
import java.util.Set;

public class homework2 {      //Please excuse the misguiding class name. I reused a blank homework document.

    //function for calculating square roots
    private static BigDecimal sqrt( int a) {
       BigDecimal lower = new BigDecimal(0.0);
       BigDecimal upper;
        for (int n = 1; (n*n) <= a; n++)
            lower = new BigDecimal(n);
        for (int i = 0; i < 101; i++) {
            upper = new BigDecimal(a).divide(lower, 150, RoundingMode.HALF_UP);
            lower = lower.add(upper).divide(new BigDecimal(2));
        }
        //lower = sqrt calculated to 99 decimal places. Decimal 100 is dropped rather than rounded
        lower = lower.setScale(99, BigDecimal.ROUND_DOWN);
        return lower;
    }

    //Removes the decimal from the given number and sums the digits together
    //Parameter is the BigDecimal you want digitally summed
    private static int numSum (BigDecimal a) {
        int total = 0;
        String sequence = a.toString();
        sequence = sequence.replace(".","");
        char[] toInt = sequence.toCharArray();  //the integers are actually characters, so the ascii code is calculated when forced to int
        Scanner s = new Scanner(sequence);
        for (char i : toInt) {
            total += (((int) i)-48);     // ascii - 48 to change the char number into an int
        }
        return total;
    }

    //A cheesy function to loop through the integers and add the digital sums together
    //Parameter is the amount of integers you want summed
    public static int solveEuler80 (int x) {
        BigDecimal so;
        int pretentious, correctAnswer = 0;

        for(int i = 1; i <= x; i++) {
            so = sqrt(i);
            pretentious = numSum(so);
            if (pretentious < 10)           //removes the sum of rational integers
                pretentious = 0;
            correctAnswer += pretentious;

            System.out.print("Natural number = " + i);                  //Some println for clarity
            System.out.print(" | Digital sum = " + pretentious);
            System.out.println(" | Current total = " + correctAnswer);
        }
            return correctAnswer;

    }

    public static void main(String[] args){
        int x = solveEuler80(100);  //The problem calls for 100
        System.out.println("Total = " + x);
    }
}
