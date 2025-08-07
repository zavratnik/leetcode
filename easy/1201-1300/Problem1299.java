import java.util.*;

public class Problem1299 {

    public static void main(String[] args) {
        int[] arr = {17, 18, 5, 4, 6, 1};
        Problem1299 solution = new Problem1299();

        int[] result = solution.replaceElements(arr);
        System.out.println(Arrays.toString(result)); // [18, 6, 6, 6, 1, -1]
    }

    public int[] replaceElements(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int temp = 0;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] > temp) {
                    temp = arr[j];
                }
            }
            if (i < arr.length - 1) {
                arr[i] = temp;
            } else if (i == arr.length - 1) {
                arr[i] = -1;
            }
        }
        return arr;
    }
}
