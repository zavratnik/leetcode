import java.util.*;

public class Problem350 {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 2, 1};
        int[] nums2 = {2, 2};
        Problem350 solution = new Problem350();

        int[] result = solution.intersect(nums1, nums2);
        System.out.println(Arrays.toString(result)); // [2, 2]
    }

    public int[] intersect(int[] nums1, int[] nums2) {
        Map<Integer, Integer> result = new HashMap<>();

        for (int num : nums1) {
            result.put(num, result.getOrDefault(num, 0) + 1);
        }

        List<Integer> final_result = new ArrayList<>();

        for (int num : nums2) {
            if (result.getOrDefault(num, 0) > 0) {
                final_result.add(num);
                result.put(num, result.get(num) - 1);
            }
        }

        int[] arr = new int[final_result.size()];
        for (int i = 0; i < final_result.size(); i++) arr[i] = final_result.get(i);
        return arr;
    }
}
