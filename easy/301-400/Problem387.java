public class Problem387 {

    public static void main(String[] args) {
        String s = "leetcode";
        Problem387 solution = new Problem387();

        int result = solution.firstUniqChar(s);
        System.out.println(result); // 0
    }

    public int firstUniqChar(String s) {
        char temp;
        if (s.length() == 1) {
            return 0;
        }
        for (int i = 0; i < s.length(); i++) {
            temp = s.charAt(i);
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == temp && j != i) {
                    break;
                } else if (j == s.length() - 1) {
                    return i;
                }
            }
        }
        return -1;
    }
}
