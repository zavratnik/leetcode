import java.util.*;

public class Problem219 {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        int k = 3;
        Problem219 solution = new Problem219();

        boolean result = solution.containsNearbyDuplicate(nums, k);
        System.out.println(result); // true
    }

    public boolean containsNearbyDuplicate(int[] nums, int k) {
        if (k <= 0) {
            return false;
        }

        Set<Integer> result = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (result.contains(nums[i])) {
                return true;
            } else {
                result.add(nums[i]);
            }
            if (result.size() > k) {
                result.remove(nums[i - k]);
            }
        }
        return false;
    }
}
