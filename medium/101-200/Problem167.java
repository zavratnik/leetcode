import java.util.*;

public class Problem167 {

    public static void main(String[] args) {
        int[] numbers = {2, 7, 11, 15};
        int target = 9;
        Problem167 solution = new Problem167();

        int[] result = solution.twoSum(numbers, target);
        System.out.println(Arrays.toString(result)); // [1, 2]
    }

    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (numbers[left] + numbers[right] != target) {
            if (target - numbers[left] < numbers[right]) {
                right--;
            }
            if (target - numbers[right] > numbers[left]) {
                left++;
            }
        }
        int[] result = new int[2];
        result[0] = left + 1;
        result[1] = right + 1;

        return result;
    }
}
