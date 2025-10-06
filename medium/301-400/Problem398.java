import java.util.*;

public class Problem398 {

    private Map<Integer, List<Integer>> map;
    private Random rand;

    public Problem398(int[] nums) {
        map = new HashMap<>();
        rand = new Random();

        for (int i = 0; i < nums.length; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
    }

    public int pick(int target) {
        List<Integer> indexi = map.get(target);
        return indexi.get(rand.nextInt(indexi.size()));
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 3, 3};
        Problem398 solution = new Problem398(nums);

        System.out.println(solution.pick(3)); // Random index of value 3 (e.g., 2, 3, or 4)
        System.out.println(solution.pick(1)); // Always 0
    }
}
