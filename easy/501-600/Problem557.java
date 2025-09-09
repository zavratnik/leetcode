public class Problem557 {

    public static void main(String[] args) {
        String s = "Let's take LeetCode contest";
        Problem557 solution = new Problem557();

        String result = solution.reverseWords(s);
        System.out.println(result); // "s'teL ekat edoCteeL tsetnoc"
    }

    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;

        int left = 0;
        for (int right = 0; right <= n; right++) {
            if (right == n || arr[right] == ' ') {
                int l = left;
                int r = right - 1;
                while (l < r) {
                    char tmp = arr[l];
                    arr[l] = arr[r];
                    arr[r] = tmp;
                    l++;
                    r--;
                }
                left = right + 1;
            }
        }
        return new String(arr);
    }
}
