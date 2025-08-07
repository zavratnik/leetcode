public class Problem747 {

    public static void main(String[] args) {
        int[] nums = {3, 6, 1, 0};
        Problem747 solution = new Problem747();

        int result = solution.dominantIndex(nums);
        System.out.println(result); // 1
    }

    public int dominantIndex(int[] nums) {
        int largest = 0;
        int second_largest = 0;
        int largest_index = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > largest) {
                second_largest = largest;
                largest = nums[i];
                largest_index = i;
            } else if (nums[i] > second_largest) {
                second_largest = nums[i];
            }
        }
        if (second_largest * 2 > largest) {
            return -1;
        } else {
            return largest_index;
        }
    }
}
