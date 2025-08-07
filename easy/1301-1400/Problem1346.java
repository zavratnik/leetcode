public class Problem1346 {

    public static void main(String[] args) {
        int[] arr = {10, 2, 5, 3};
        Problem1346 solution = new Problem1346();

        boolean result = solution.checkIfExist(arr);
        System.out.println(result); // true
    }

    public boolean checkIfExist(int[] arr) {
        boolean result = false;

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (i != j && arr[i] == arr[j] * 2) {
                    result = true;
                }
            }
        }

        return result;
    }
}
