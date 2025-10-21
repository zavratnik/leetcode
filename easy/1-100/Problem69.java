public class Problem69 {

    public static void main(String[] args) {
        int x = 8;
        Problem69 solution = new Problem69();

        int result = solution.mySqrt(x);
        System.out.println(result); // 2
    }

    public int mySqrt(int x) {
        int left = 0;
        int right = x / 2;

        if (x < 2) {
            return x;
        }

        while (left <= right) {
            int middle = (left + right) / 2;
            long square = (long) middle * middle;

            if (square < x) {
                left = middle + 1;
            } else if (square > x) {
                right = middle - 1;
            } else {
                return middle;
            }
        }
        return right;
    }
}
