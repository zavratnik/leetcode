public class Problem680 {

    public static void main(String[] args) {
        String s = "abca";
        Problem680 solution = new Problem680();

        boolean result = solution.validPalindrome(s);
        System.out.println(result); // true
    }

    public boolean validPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                int l1 = left + 1, r1 = right;
                boolean ok1 = true;
                while (l1 < r1) {
                    if (s.charAt(l1++) != s.charAt(r1--)) {
                        ok1 = false;
                        break;
                    }
                }
                if (ok1) return true;

                int l2 = left, r2 = right - 1;
                while (l2 < r2) {
                    if (s.charAt(l2++) != s.charAt(r2--)) {
                        return false;
                    }
                }
                return true;
            } else {
                left++;
                right--;
            }
        }
        return true;
    }
}
