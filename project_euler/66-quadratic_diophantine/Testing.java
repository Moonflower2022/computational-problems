

class QuickStart {
    public static void main (String[] args) {
        System.out.println(y(8, 7));
        long x = 10861079;
        System.out.println(x * x);

    }

    public static double y (int x, int d) {
        return (double) Math.sqrt((double) (x * x - 1) / d);
    }

    public static boolean isInt (double number) {
        return (int) number == number;
    }
}