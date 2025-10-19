public class Problem389 {

    public static void main(String[] args) {
        String s = "abcd";
        String t = "abcde";
        Problem389 solution = new Problem389();

        char result = solution.findTheDifference(s, t);
        System.out.println(result); // e
    }

    public char findTheDifference(String s, String t) {
        int tempA = 0;
        int tempB = 0;

        for (int i = 0; i < s.length(); i++) {
            tempA += 'a' - s.charAt(i);
        }
        for (int j = 0; j < t.length(); j++) {
            tempB += 'a' - t.charAt(j);
        }

        int result = 'a' - (tempB - tempA);

        return (char) result;
    }
}
