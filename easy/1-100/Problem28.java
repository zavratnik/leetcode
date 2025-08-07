public class Problem28 {

    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "ll";
        Problem28 solution = new Problem28();

        int result = solution.strStr(haystack, needle);
        System.out.println(result); // 2
    }

    public int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}
