/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Problem278 extends VersionControl {

    public static void main(String[] args) {
        // Example cannot be directly executed since isBadVersion() is provided by LeetCode.
        // Use LeetCode environment to test.
    }

    public int firstBadVersion(int n) {
        int left = 1;
        int right = n;

        while (left < right) {
            int middle = left + (right - left) / 2;

            if (isBadVersion(middle)) {
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return left;
    }
}
