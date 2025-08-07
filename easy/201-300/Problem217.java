import java.util.*;

public class Problem217 {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 1};
        Problem217 solution = new Problem217();

        boolean result = solution.containsDuplicate(nums);
        System.out.println(result); // true
    }

    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }

        return false;
    }
}
