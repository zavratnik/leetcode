import java.util.*;

public class Problem1051 {

    public static void main(String[] args) {
        int[] heights = {1, 1, 4, 2, 1, 3};
        Problem1051 solution = new Problem1051();

        int result = solution.heightChecker(heights);
        System.out.println(result); // 3
    }

    public int heightChecker(int[] heights) {
        int[] sorted = Arrays.copyOf(heights, heights.length);
        int counter = 0;
        Arrays.sort(sorted);

        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != sorted[i]) {
                counter++;
            }
        }

        return counter;
    }
}
