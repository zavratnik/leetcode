public class Problem485 {

    public static void main(String[] args) {
        int[] nums = {1, 1, 0, 1, 1, 1};
        Problem485 solution = new Problem485();

        int result = solution.findMaxConsecutiveOnes(nums);
        System.out.println(result); // 3
    }

    public int findMaxConsecutiveOnes(int[] nums) {
        int longest = 0;
        int temp = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                temp += 1;
            } else {
                if (temp > longest) {
                    longest = temp;
                }
                temp = 0;
            }
        }
        if (temp > longest) {
            longest = temp;
        }
        return longest;
    }
}
