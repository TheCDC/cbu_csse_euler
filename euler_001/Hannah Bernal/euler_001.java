public class Main {

    public static void main(String[] args) {
        int sum = 0;
        //boundaries 3-1000

        for (int i = 3; i < 1000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
//                System.out.print(i + " ");
            }
        }
        System.out.println(sum);
    }
}
