import java.util.*;

public class Problem128 {

    public static void main(String[] args) {
        int[] nums = {100, 4, 200, 1, 3, 2};
        Problem128 solution = new Problem128();

        int result = solution.longestConsecutive(nums);
        System.out.println(result); // 4
    }

    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int max = 1;
        int temp = 1;

        for (int i = 0; i < nums.length; i++) {
            if (i + 1 != nums.length && nums[i] + 1 == nums[i + 1]) {
                temp++;
            } else if (i + 1 != nums.length && nums[i] == nums[i + 1]) {
                continue;
            } else {
                max = Math.max(max, temp);
                temp = 1;
            }
        }

        return max;
    }
}
