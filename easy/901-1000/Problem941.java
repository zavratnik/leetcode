public class Problem941 {

    public static void main(String[] args) {
        int[] arr = {0, 3, 2, 1};
        Problem941 solution = new Problem941();

        boolean result = solution.validMountainArray(arr);
        System.out.println(result); // true
    }

    public boolean validMountainArray(int[] arr) {
        int i = 0;
        int n = arr.length;

        if (n < 3) return false;

        while (i + 1 < n && arr[i] < arr[i + 1]) {
            i++;
        }

        if (i == 0 || i == n - 1) return false;

        while (i + 1 < n && arr[i] > arr[i + 1]) {
            i++;
        }

        return i == n - 1;
    }
}
