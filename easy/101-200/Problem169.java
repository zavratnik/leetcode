import java.util.*;

public class Problem169 {

    public static void main(String[] args) {
        int[] nums = {3, 2, 3};
        Problem169 solution = new Problem169();

        int result = solution.majorityElement(nums);
        System.out.println(result); // 3
    }

    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }

        return Collections.max(map.entrySet(), Map.Entry.comparingByValue()).getKey();
    }
}
