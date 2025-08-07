
public class Problem11 {

    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        Problem11 solution = new Problem11();

        int result = solution.maxArea(height);
        System.out.println(result); // 49
    }

    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int temp = Math.min(height[left], height[right]) * (right - left);
            maxArea = Math.max(maxArea, temp);

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }
        }

        return maxArea;
    }
}
