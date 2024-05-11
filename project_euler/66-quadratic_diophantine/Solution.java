class Solution {
    public static void main (String[] args) {
        long max_d = 0;
        long max_x = 0;

        for (long d = 1; d < 1000; d++) {
            System.out.println(d);
            if (isLong(Math.sqrt(d))) {continue;}
            long x = 0;
            while (!isLong(y(x, d)) || y(x, d) == 0) {
                x += 1;
            }
            if (x > max_x) {
                max_d = d;
                max_x = x;
            }
        }
        System.out.println(max_x);
        System.out.println(max_d);
        System.out.println(y(max_x, max_d));
        System.out.println(max_x * max_x - max_d * y(max_x, max_d) * y(max_x, max_d));
    }

    public static boolean isLong (double number) {
        return (long) number == number;
    }

    public static double y (long x, long d) {
        return (double) Math.sqrt((double) (x * x - 1) / d);
    }
}