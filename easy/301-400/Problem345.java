import java.util.*;

public class Problem345 {

    public static void main(String[] args) {
        String s = "leetcode";
        Problem345 solution = new Problem345();

        String result = solution.reverseVowels(s);
        System.out.println(result); // leotcede
    }

    public String reverseVowels(String s) {
        int left = 0;
        int right = s.length() - 1;

        Set<Character> samoglasniki = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');

        char[] chars = s.toCharArray();

        while (left < right) {
            while (left < right && !samoglasniki.contains(chars[left])) {
                left++;
            }
            while (left < right && !samoglasniki.contains(chars[right])) {
                right--;
            }
            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;

            left++;
            right--;
        }
        return new String(chars);
    }
}
