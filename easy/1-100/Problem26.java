public class Problem26 {

    public static void main(String[] args) {
        int[] nums = {1, 1, 2};
        Problem26 solution = new Problem26();

        int result = solution.removeDuplicates(nums);
        System.out.println(result); // 2

        for (int i = 0; i < result; i++) {
            System.out.print(nums[i] + " "); // 1 2 
        }
        System.out.println();
    }

    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int counter = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[counter - 1]) {
                nums[counter] = nums[i];
                counter++;
            }
        }

        return counter;
    }
}
