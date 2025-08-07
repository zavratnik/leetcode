import java.util.*;

public class Problem1 {

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        Problem1 solution = new Problem1();

        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result)); // [0, 1]
    }

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> stevila = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int middleman = target - nums[i];

            if (stevila.containsKey(middleman)) {
                return new int[] {stevila.get(middleman), i};
            }
            stevila.put(nums[i], i);
        }
        return new int[0];
    }
}
