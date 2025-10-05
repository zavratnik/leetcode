import java.util.*;

public class Problem832 {

    public static void main(String[] args) {
        int[][] image = {
            {1, 1, 0},
            {1, 0, 1},
            {0, 0, 0}
        };
        Problem832 solution = new Problem832();

        int[][] result = solution.flipAndInvertImage(image);
        for (int[] row : result) {
            System.out.println(Arrays.toString(row));
        }
        // Output:
        // [1, 0, 0]
        // [0, 1, 0]
        // [1, 1, 1]
    }

    public int[][] flipAndInvertImage(int[][] image) {
        for (int i = 0; i < image.length; i++) {
            int left = 0;
            int right = image[i].length - 1;

            while (left <= right) {
                if (image[i][left] == image[i][right]) {
                    image[i][left] ^= 1;
                    if (left != right) image[i][right] ^= 1;
                }
                left++;
                right--;
            }
        }
        return image;
    }
}
