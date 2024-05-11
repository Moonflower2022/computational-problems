class Solution {
    public static void main(String[] args) {
        long minimumD = -1;
        for (int i = 2; ; i++) {
            if (minimumD != -1 && pentagonNumber(i) - pentagonNumber(i - 1) >= minimumD) {
                break;
            }
            for (int j = i - 1; j >= 1; j--) {
                long difference = pentagonNumber(i) - pentagonNumber(j);
                if (minimumD != -1 && difference >= minimumD) {
                    break;
                }
                if (isPentagonal(pentagonNumber(i) + pentagonNumber(j)) && isPentagonal(difference)) {
                    minimumD = difference;
                }
            }
        }
        System.out.println(minimumD);
    }

    private static boolean isPentagonal(long y) {
		if (y <= 0)
			return false;
	
		long temp = y * 24 + 1;
		long sqrt = sqrt(temp);
		return sqrt * sqrt == temp && sqrt % 6 == 5;
	}

    private static long sqrt(long x) {
		if (x < 0)
			throw new IllegalArgumentException("Square root of negative number");
		long y = 0;
		for (long i = 1L << 31; i != 0; i >>>= 1) {
			y |= i;
			if (y > 3037000499L || y * y > x)
				y ^= i;
		}
		return y;
	}

    public static long pentagonNumber(int i) {
        return (long) i * (3 * i - 1) / 2;
    }
}
