public class Problem74 {

    public static void main(String[] args) {
        int[][] image = {
            {1, 3, 5, 7},
            {10, 11, 16, 20},
            {23, 30, 34, 60}
        };
        int target = 3;
        Problem74 solution = new Problem74();

        boolean result = solution.searchMatrix(image, target);
        System.out.println(result); // true
    }

    public boolean searchMatrix(int[][] image, int target) {
        if (image == null || image.length == 0 || image[0].length == 0) {
            return false;
        }

        int leftStolpec = 0;
        int rightStolpec = image.length - 1;
        int rightVrstica = image[0].length - 1;

        while (leftStolpec <= rightStolpec) {
            int middleStolpec = leftStolpec + (rightStolpec - leftStolpec) / 2;

            int firstVal = image[middleStolpec][0];
            int lastVal = image[middleStolpec][rightVrstica];

            if (target < firstVal) {
                rightStolpec = middleStolpec - 1;
            } else if (target > lastVal) {
                leftStolpec = middleStolpec + 1;
            } else {
                int leftVrstica = 0;
                int rV = rightVrstica;

                while (leftVrstica <= rV) {
                    int middleVrstica = leftVrstica + (rV - leftVrstica) / 2;
                    int valueVrstica = image[middleStolpec][middleVrstica];

                    if (valueVrstica == target) {
                        return true;
                    }
                    if (valueVrstica < target) {
                        leftVrstica = middleVrstica + 1;
                    } else {
                        rV = middleVrstica - 1;
                    }
                }
                return false;
            }
        }
        return false;
    }
}
