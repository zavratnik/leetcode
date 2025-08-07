import java.util.*;

public class Problem9 {

    public static void main(String[] args) {
        int x = 121;
        Problem9 solution = new Problem9();

        boolean result = solution.isPalindrome(x);
        System.out.println(result); // true
    }

    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        List<Integer> stevilo = new ArrayList<>();

        while (x > 0) {
            int ostanek = x % 10;
            x = x / 10;
            stevilo.add(ostanek);
        }

        int left = 0;
        int right = stevilo.size() - 1;

        while (left < right) {
            if (!stevilo.get(left).equals(stevilo.get(right))) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
