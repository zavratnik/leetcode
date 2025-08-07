import java.util.*;

public class Problem66 {

    public static void main(String[] args) {
        int[] digits = {9, 9, 9};
        Problem66 solution = new Problem66();

        int[] result = solution.plusOne(digits);
        System.out.println(Arrays.toString(result)); // [1, 0, 0, 0]
    }

    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }

        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }
}
