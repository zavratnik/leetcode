public class Problem383 {

    public static void main(String[] args) {
        String ransomNote = "aa";
        String magazine = "aab";
        Problem383 solution = new Problem383();

        boolean result = solution.canConstruct(ransomNote, magazine);
        System.out.println(result); // true
    }

    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()) return false;

        int[] baza = new int[26];
        for (int i = 0; i < magazine.length(); i++) {
            baza[magazine.charAt(i) - 'a'] += 1;
        }

        for (int j = 0; j < ransomNote.length(); j++) {
            if ((baza[ransomNote.charAt(j) - 'a'] -= 1) < 0) return false;
        }

        return true;
    }
}
