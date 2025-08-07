import java.util.*;

public class Problem448 {

    public static void main(String[] args) {
        int[] nums = {4, 3, 2, 7, 8, 2, 3, 1};
        Problem448 solution = new Problem448();

        List<Integer> result = solution.findDisappearedNumbers(nums);
        System.out.println(result); // [5, 6]
    }

    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> numbers = new ArrayList<>();

        Arrays.sort(nums);
        int readPointer = 0;

        for (int j = 1; j <= nums.length; j++) {
            while (readPointer < nums.length && nums[readPointer] < j) {
                readPointer++;
            }
            if (readPointer >= nums.length || nums[readPointer] != j) {
                numbers.add(j);
            } else {
                readPointer++;
            }
        }
        return numbers;
    }
}
