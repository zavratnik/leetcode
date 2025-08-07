public class Problem242 {

    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        Problem242 solution = new Problem242();

        boolean result = solution.isAnagram(s, t);
        System.out.println(result); // true
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
