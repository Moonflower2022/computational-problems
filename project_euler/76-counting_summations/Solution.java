class Solution {
    public static void main (String[] args) {
        int input = 35;
        System.out.println((countingSummations(input))/2);

    }

    public static int countingSummations (int input) {
        if (input <= 2) {
            return input;
        }
        int sum = 0;
        for (int i = 1; i < input; i++) {
            sum += countingSummations(input - i);
        }
        return sum;
    }
}