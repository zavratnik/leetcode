import java.util.*;

public class Problem347 {

    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = 2;
        Problem347 solution = new Problem347();

        int[] result = solution.topKFrequent(nums, k);
        System.out.println(Arrays.toString(result)); // [1, 2]
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> stevila = new HashMap<>();

        for (int num : nums) {
            stevila.merge(num, 1, Integer::sum);
        }

        int[] topN = stevila.entrySet()
                .stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .limit(k)
                .mapToInt(entry -> entry.getKey())
                .toArray();

        return topN;
    }
}
