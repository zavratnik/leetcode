public class Problem287 {

    public static void main(String[] args) {
        int[] nums = {1, 3, 4, 2, 2};
        Problem287 solution = new Problem287();

        int result = solution.findDuplicate(nums);
        System.out.println(result); // 2
    }

    public int findDuplicate(int[] nums) {
        int left = 1;
        int right = nums.length - 1;

        while (left < right) {
            int middle = left + (right - left) / 2;
            int counter = 0;

            for (int x : nums) {
                if (x <= middle) {
                    counter++;
                }
            }

            if (counter > middle) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return right;
    }
}
