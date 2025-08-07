import java.util.*;

public class Problem283 {

    public static void main(String[] args) {
        int[] nums = {0, 1, 0, 3, 12};
        Problem283 solution = new Problem283();

        solution.moveZeroes(nums);
        System.out.println(Arrays.toString(nums)); // [1, 3, 12, 0, 0]
    }

    public void moveZeroes(int[] nums) {
        int writePointer = 0;
        int length = nums.length;
        for (int readPointer = 0; readPointer < length - writePointer; readPointer++) {
            if (nums[readPointer] == 0) {
                for (int j = readPointer; j < nums.length - 1; j++) {
                    nums[j] = nums[j + 1];
                }
                nums[length - 1] = 0;
                writePointer++;
                readPointer--;
            }
        }
    }
}
