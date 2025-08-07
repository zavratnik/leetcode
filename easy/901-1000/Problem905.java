import java.util.*;

public class Problem905 {

    public static void main(String[] args) {
        int[] nums = {3, 1, 2, 4};
        Problem905 solution = new Problem905();

        int[] result = solution.sortArrayByParity(nums);
        System.out.println(Arrays.toString(result)); // [2, 4, 3, 1]
    }

    public int[] sortArrayByParity(int[] nums) {
        int counter = 0;
        int temp = 0;
        int length = nums.length;
        for (int i = 0; i < nums.length - counter; i++) {
            if (nums[i] % 2 != 0) {
                temp = nums[i];
                for (int j = i; j < nums.length - 1; j++) {
                    nums[j] = nums[j + 1];
                }
                nums[length - 1] = temp;
                counter++;
                i--;
            }
        }
        return nums;
    }
}
