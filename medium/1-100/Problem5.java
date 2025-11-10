public class Problem5 {

    public static void main(String[] args) {
        String s = "babad";
        Problem5 solution = new Problem5();

        String result = solution.longestPalindrome(s);
        System.out.println(result); // "bab" or "aba"
    }

    public String longestPalindrome(String s) {
        String longest = "";
        int left;
        int right;

        for (int i = 0; i < s.length(); i++) {
            left = i;
            right = i + 1;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            longest = longest.length() > s.substring(left + 1, right).length()
                    ? longest
                    : s.substring(left + 1, right);

            left = i;
            right = i;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
            }
            longest = longest.length() > s.substring(left + 1, right).length()
                    ? longest
                    : s.substring(left + 1, right);
        }

        return longest;
    }
}
