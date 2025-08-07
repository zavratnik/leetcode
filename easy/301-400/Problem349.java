import java.util.*;

public class Problem349 {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 2, 1};
        int[] nums2 = {2, 2};
        Problem349 solution = new Problem349();

        int[] result = solution.intersection(nums1, nums2);
        System.out.println(Arrays.toString(result)); // [2]
    }

    public int[] intersection(int[] nums1, int[] nums2) {
        Map<Integer, Integer> stevila = new HashMap<>();

        for (int i = 0; i < nums1.length; i++) {
            if (!(stevila.containsKey(nums1[i]))) {
                stevila.put(nums1[i], 0);
            }
        }
        for (int j = 0; j < nums2.length; j++) {
            if (stevila.containsKey(nums2[j])) {
                stevila.put(nums2[j], 1);
            }
        }

        stevila.entrySet().removeIf(entry -> entry.getValue() < 1);

        int[] result = stevila.keySet().stream().mapToInt(Integer::intValue).toArray();

        return result;
    }
}
