public class Problem367 {

    public static void main(String[] args) {
        int num = 16;
        Problem367 solution = new Problem367();

        boolean result = solution.isPerfectSquare(num);
        System.out.println(result); // true
    }

    public boolean isPerfectSquare(int num) {
        int left = 1;
        int right = num;

        if (num == 1) return true;

        while (left < right) {
            int middle = left + (right - left) / 2;
            long sq = (long) middle * middle;

            if (sq > num) {
                right = middle;
            } else if (sq < num) {
                left = middle + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
