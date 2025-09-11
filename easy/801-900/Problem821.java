import java.util.*;

public class Problem821 {

    public static void main(String[] args) {
        String s = "loveleetcode";
        char c = 'e';
        Problem821 solution = new Problem821();

        int[] result = solution.shortestToChar(s, c);
        System.out.println(Arrays.toString(result)); // [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
    }

    public int[] shortestToChar(String s, char c) {
        int length = s.length();
        int[] result = new int[length];

        int left = 0;
        int curr = 0;
        int right = 0;

        while (left < length && right < length) {
            while (right < length - 1 && s.charAt(right) != c) {
                right++;
            }

            while (right < length && curr <= right) {
                if (s.charAt(right) == c && s.charAt(left) == c) {
                    result[curr] = Math.min(Math.abs(curr - left), Math.abs(curr - right));
                } else if (s.charAt(left) == c && s.charAt(right) != c) {
                    result[curr] = Math.abs(curr - left);
                } else if (s.charAt(left) != c && s.charAt(right) == c) {
                    result[curr] = Math.abs(curr - right);
                }
                curr++;
            }
            left = right;
            right++;
        }

        return result;
    }
}
