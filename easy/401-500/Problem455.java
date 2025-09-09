import java.util.*;

public class Problem455 {

    public static void main(String[] args) {
        int[] g = {1, 2, 3};
        int[] s = {1, 1};
        Problem455 solution = new Problem455();

        int result = solution.findContentChildren(g, s);
        System.out.println(result); // 1
    }

    public int findContentChildren(int[] g, int[] s) {
        int left = g.length - 1;
        int right = s.length - 1;

        int counter = 0;

        Arrays.sort(g);
        Arrays.sort(s);

        while (left >= 0 && right >= 0) {
            if (g[left] <= s[right]) {
                counter++;
                left--;
                right--;
            } else {
                left--;
            }
        }
        return counter;
    }
}
