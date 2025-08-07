public class Problem121 {

    public static void main(String[] args) {
        int[] prices = {7, 1, 5, 3, 6, 4};
        Problem121 solution = new Problem121();

        int result = solution.maxProfit(prices);
        System.out.println(result); // 5
    }

    public int maxProfit(int[] prices) {
        int low = 0;
        int high = 1;
        int maxProfit = 0;

        if (prices.length == 1) {
            return 0;
        }

        while (high < prices.length) {
            if (prices[low] < prices[high]) {
                maxProfit = Math.max(maxProfit, prices[high] - prices[low]);
            } else {
                low = high;
            }
            high++;
        }
        return maxProfit;
    }
}
