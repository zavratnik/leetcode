/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return       -1 if num is higher than the picked number
 *                1 if num is lower than the picked number
 *                otherwise return 0
 * int guess(int num);
 */

public class Problem374 extends GuessGame {

    public static void main(String[] args) {
        // Example cannot be executed locally because guess() is provided by LeetCode.
        // Test this solution directly in the LeetCode environment.
    }

    public int guessNumber(int n) {
        int left = 1;
        int right = n;

        while (left <= right) {
            int middle = left + (right - left) / 2;
            int res = guess(middle);

            if (res == -1) {
                right = middle - 1;
            } else if (res == 1) {
                left = middle + 1;
            } else {
                return middle;
            }
        }
        return 0;
    }
}
