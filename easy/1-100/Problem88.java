import java.util.*;

public class Problem88 {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int m = 3;
        int[] nums2 = {2, 5, 6};
        int n = 3;
        Problem88 solution = new Problem88();

        solution.merge(nums1, m, nums2, n);
        System.out.println(Arrays.toString(nums1)); // [1, 2, 2, 3, 5, 6]
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int counter = 0;

        for (int i = m; i < m + n; i++) {
            nums1[i] = nums2[counter];
            counter++;
        }
        Arrays.sort(nums1);
    }
}
