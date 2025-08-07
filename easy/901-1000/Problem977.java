import java.util.*;

public class Problem977 {

    public static void main(String[] args) {
        int[] nums = {-4, -1, 0, 3, 10};
        Problem977 solution = new Problem977();

        int[] result = solution.sortedSquares(nums);
        System.out.println(Arrays.toString(result)); // [0, 1, 9, 16, 100]
    }

    public int[] sortedSquares(int[] nums) {
        int[] temp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            temp[i] = nums[i] * nums[i];
        }
        Arrays.sort(temp);
        return temp;
    }
}
