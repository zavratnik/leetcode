import java.util.*;

public class Problem414 {

    public static void main(String[] args) {
        int[] nums = {2, 2, 3, 1};
        Problem414 solution = new Problem414();

        int result = solution.thirdMax(nums);
        System.out.println(result); // 1
    }

    public int thirdMax(int[] nums) {
        Arrays.sort(nums);

        int length = nums.length;
        int counter = length - 1;
        int position = 1;
        int[] temp = new int[length];
        temp[0] = nums[0];

        for (int i = 1; i < length; i++) {
            if (nums[i] != nums[i - 1]) {
                counter--;
                temp[position] = nums[i];
                position++;
            }
        }
        int length_final = length - counter;
        int[] final_arrray = new int[length_final];
        for (int j = 0; j < final_arrray.length; j++) {
            final_arrray[length_final - 1] = temp[j];
            length_final--;
        }
        if (final_arrray.length >= 3) {
            return final_arrray[2];
        } else return final_arrray[0];
    }
}
