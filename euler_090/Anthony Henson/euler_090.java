import java.util.ArrayList;
import java.util.Arrays;

public class euler_090 {

    public void swap (ArrayList<Integer> d, int a, int b) {
        int c = d.get(a);
        d.set(a, d.get(b));
        d.set(b, c);
    }
    //Heap's algorithm for generating permutations
    public void heapPermutation (ArrayList<String> b, ArrayList<Integer> a, int size, int n) {
        // if size becomes 1 then prints the obtained
        // permutation
        if (size == 1)
        {
            String builder = "";
            for (int i = 0; i < a.size(); i++) {
                builder += a.get(i);
            }
            b.add(builder);
        }
        for (int i=0; i<size; i++) {
            heapPermutation(b, a, size - 1, n);

            // if size is odd, swap first and last
            // element
            if (size % 2 == 1)
                swap(a, 0, size - 1);

                // If size is even, swap ith and last
                // element
            else
                swap(a, i, size - 1);
        }
    }

    //sorts the characters in a string
    public String sortString (String start) {
        char[] breaker = start.toCharArray();
        Arrays.sort(breaker);
        return new String(breaker);
    }

    //turns a string of ints into an ArrayList<Integer>
    public ArrayList<Integer> stringToIntegerArrayList (String x) {
        char[] xArray = x.toCharArray();
        ArrayList<Integer> getArrayList = new ArrayList<>();

        for (char y : xArray) {
            getArrayList.add(y - '0');
        }

        return getArrayList;
    }

    //n <= 9 or heap error
    //because numerals starts at 0, this actually calculates n+1Choose10, so nCk(9, 10) will give 1 result of the full string numerals
    public ArrayList nCk (int n, int k) {
        ArrayList<String> combinations = new ArrayList();
        ArrayList<Integer> numerals = new ArrayList<>();
        //Integer[] visualAid = new Integer[]{0,1,2,3,4,5,6,7,8,9};

        for (int i = 0; i <= n; i++) {
            numerals.add(i);
        }

        //Todo add a try/catch for n > 9
        ArrayList<String> bigArrayList = new ArrayList<>();
        heapPermutation(bigArrayList, numerals, numerals.size(), numerals.size());

        for (int x = 0; x < bigArrayList.size(); x++) {
            ArrayList<Integer> smallArrayList = new ArrayList(stringToIntegerArrayList(bigArrayList.get(x)));

            for (int y = 0; y <= smallArrayList.size() - k; y++) {
                String combBuilder = "";
                for (int z = y; z < y + k; z++) {
                    combBuilder += smallArrayList.get(z);
                }
                if (!combinations.contains(sortString(combBuilder))){
                    combinations.add(sortString(combBuilder));
                }
            }
        }
        return combinations;
    }

    //adds either a 6 or a 9 if one of them is present
    public char[] checkPrimesHelper (ArrayList<String> currentBlock, ArrayList<String> editedBlock, int index) {
        String blockHolder = currentBlock.get(index);
        if (currentBlock.get(index).contains("6") && !currentBlock.get(index).contains("9")) {
            editedBlock.set(index, currentBlock.get(index) + "9");
            blockHolder = editedBlock.get(index);
        } else if (currentBlock.get(index).contains("9") && !currentBlock.get(index).contains("6")) {
            editedBlock.set(index, currentBlock.get(index) + "6");
            blockHolder = editedBlock.get(index);
        }
        return blockHolder.toCharArray();
    }

    //main logic that spins the blockas around checking if ti satisfies all cases of prime numbers
    public void checkPrimes (ArrayList<String> sets, ArrayList<String> blocks, String[] primes) {
        ArrayList<String> blocksEdited = new ArrayList<>(blocks); //copy of blocks array for editing
        for (int i = 0; i < blocks.size() - 1; i++) {
            char[] block1 = blocks.get(i).toCharArray();
            char[] block1Holder = checkPrimesHelper(blocks, blocksEdited, i);

            //create a new copy of the array of primes for editing
            for (int j = i + 1; j < blocks.size(); j++) {
                ArrayList<String> primeArray = new ArrayList<>();
                for (String z : primes) {
                    primeArray.add(z);
                }

                char[] block2 = blocks.get(j).toCharArray();
                char[] block2Holder = checkPrimesHelper(blocks, blocksEdited, j);

                //loops through the two char arrays checking int combinations against the array of primes
                spinLoop:
                for (char a : block1Holder) {
                    for (char b : block2Holder) {
                        //couldn't think of a better way to add 2 characters to a string
                        String value1 = "";
                        String value2 = "";
                        value1 += a;
                        value1 += b;
                        value2 += b;
                        value2 += a;

                        //if the array of primes is empty add the two blocks to the set arrayList
                        if (primeArray.size() == 0) {
                                sets.add(Arrays.toString(block1));
                                sets.add(Arrays.toString(block2));
                            break spinLoop;
                        }
                        //if the combination is in the array of primes then remove the prime from the array
                        if (primeArray.contains(value1)) {
                            primeArray.remove(primeArray.indexOf(value1));
                        }
                        if (primeArray.contains(value2)) {
                            primeArray.remove(primeArray.indexOf(value2));
                        }
                    }
                }
            }
        }
    }

    public static void  main (String[] args) {

        String[] primeNumbers = new String[]{"01", "04", "09", "16", "25", "36", "49", "64", "81"};
        euler_090 e090 = new euler_090();
        ArrayList<String> possibleCombinations = e090.nCk(9,6);
        //System.out.println("Number of combinations: " + possibleCombinations.size());
        //System.out.println("List of combinations: \n" + possibleCombinations.toString());

        ArrayList<String> primeArrangements = new ArrayList<>();
        e090.checkPrimes(primeArrangements, possibleCombinations, primeNumbers);
        //System.out.println("List of prime number sets: \n" + primeArrangements.toString());
        //System.out.println("Answer: ");
        System.out.println(primeArrangements.size()/2);
    }
}
