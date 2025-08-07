public class Problem1672 {

    public static void main(String[] args) {
        int[][] accounts = {{1, 2, 3}, {3, 2, 1}};
        Problem1672 solution = new Problem1672();

        int result = solution.maximumWealth(accounts);
        System.out.println(result); // 6
    }

    public int maximumWealth(int[][] accounts) {
        int sum = 0;
        for (int i = 0; i < accounts.length; i++) {
            int temp = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                temp += accounts[i][j];
            }
            sum = Math.max(sum, temp);
        }
        return sum;
    }
}
