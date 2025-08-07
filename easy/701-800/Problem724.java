public class Problem724 {

    public static void main(String[] args) {
        int[] nums = {1, 7, 3, 6, 5, 6};
        Problem724 solution = new Problem724();

        int result = solution.pivotIndex(nums);
        System.out.println(result); // 3
    }

    public int pivotIndex(int[] nums) {
        int leftSum = 0;
        for (int i = 0; i < nums.length; i++) {
            int rightSum = 0;
            for (int j = i + 1; j < nums.length; j++) {
                rightSum += nums[j];
            }
            if (rightSum == 0 && i == 0) {
                return 0;
            }
            if (rightSum == leftSum) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
}
