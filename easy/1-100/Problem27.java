public class Problem27 {

    public static void main(String[] args) {
        int[] nums = {3, 2, 2, 3};
        int val = 3;
        Problem27 solution = new Problem27();

        int result = solution.removeElement(nums, val);
        System.out.println(result); // 2

        for (int i = 0; i < result; i++) {
            System.out.print(nums[i] + " "); // 2 2 
        }
        System.out.println();
    }

    public int removeElement(int[] nums, int val) {
        int counter = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[counter] = nums[j];
                counter++;
            }
        }
        return counter;
    }
}
