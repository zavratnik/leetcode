public class Problem268 {

    public static void main(String[] args) {
        int[] nums = {3, 0, 1};
        Problem268 solution = new Problem268();

        int result = solution.missingNumber(nums);
        System.out.println(result); // 2
    }

    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;

        for (int num : nums) {
            actualSum += num;
        }

        return expectedSum - actualSum;
    }
}
