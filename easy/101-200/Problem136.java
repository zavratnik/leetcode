public class Problem136 {

    public static void main(String[] args) {
        int[] nums = {4, 1, 2, 1, 2};
        Problem136 solution = new Problem136();

        int result = solution.singleNumber(nums);
        System.out.println(result); // 4
    }

    public int singleNumber(int[] nums) {
        int ans = 0;
        for (int i : nums) {
            ans ^= i;
        }
        return ans;
    }
}
