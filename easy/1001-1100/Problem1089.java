import java.util.*;

public class Problem1089 {

    public static void main(String[] args) {
        int[] arr = {1, 0, 2, 3, 0, 4, 5, 0};
        Problem1089 solution = new Problem1089();

        solution.duplicateZeros(arr);
        System.out.println(Arrays.toString(arr)); // [1, 0, 0, 2, 3, 0, 0, 4]
    }

    public void duplicateZeros(int[] arr) {
        for (int i = arr.length - 1; i > 0; i--) {
            if (arr[i - 1] == 0) {
                for (int j = arr.length - 1; j >= i; j--) {
                    arr[j] = arr[j - 1];
                }
            }
        }
    }
}
