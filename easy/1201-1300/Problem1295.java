public class Problem1295 {

    public static void main(String[] args) {
        int[] nums = {12, 345, 2, 6, 7896};
        Problem1295 solution = new Problem1295();

        int result = solution.findNumbers(nums);
        System.out.println(result); // 2
    }

    public int findNumbers(int[] nums) {
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            int digits = String.valueOf(nums[i]).length();
            if (digits % 2 == 0) {
                counter += 1;
            }
        }
        return counter;
    }
}
