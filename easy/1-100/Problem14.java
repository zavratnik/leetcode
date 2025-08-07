public class Problem14 {

    public static void main(String[] args) {
        String[] strs = {"flower", "flow", "flight"};
        Problem14 solution = new Problem14();

        String result = solution.longestCommonPrefix(strs);
        System.out.println(result); // fl
    }

    public String longestCommonPrefix(String[] strs) {
        String first_string = strs[0];

        if (strs.length == 1) {
            return strs[0];
        }

        for (int i = 1; i < strs.length; i++) {
            if (!(strs[i].startsWith(first_string))) {
                first_string = first_string.substring(0, first_string.length() - 1);
                i--;
            } else if (strs[i].startsWith(first_string) && i == strs.length - 1) {
                return first_string;
            }
            if (first_string.length() == 0) {
                return "";
            }
        }
        return "";
    }
}
