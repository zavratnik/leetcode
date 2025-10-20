public class Problem409 {

    public static void main(String[] args) {
        String s = "abccccdd";
        Problem409 solution = new Problem409();

        int result = solution.longestPalindrome(s);
        System.out.println(result); // 7
    }

    public int longestPalindrome(String s) {
        int[] mapa = new int[128];
        int counter = 0;
        boolean liho = false;

        for (int i = 0; i < s.length(); i++) {
            mapa[s.charAt(i)]++;
        }

        for (int map : mapa) {
            counter += (map / 2) * 2;
            if (map % 2 != 0) {
                liho = true;
            }
        }

        return liho ? counter + 1 : counter;
    }
}
