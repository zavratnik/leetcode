import java.util.*;

public class Problem238 {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4};
        Problem238 solution = new Problem238();

        int[] result = solution.productExceptSelf(nums);
        System.out.println(Arrays.toString(result)); // [24, 12, 8, 6]
    }

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        answer[0] = 1;
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        int rightProduct = 1;
        for (int j = n - 1; j >= 0; j--) {
            answer[j] = answer[j] * rightProduct;
            rightProduct = rightProduct * nums[j];
        }

        return answer;
    }
}
