import java.util.*;

public class Problem290 {

    public static void main(String[] args) {
        String pattern = "abba";
        String s = "dog cat cat dog";
        Problem290 solution = new Problem290();

        boolean result = solution.wordPattern(pattern, s);
        System.out.println(result);
    }

    public boolean wordPattern(String pattern, String s) {
        Map<Character, String> result = new HashMap<>();

        int counter = 0;

        for (int i = 0; i < pattern.length(); i++) {
            if (counter >= s.length()) return false;

            StringBuilder sb = new StringBuilder();
            while (counter < s.length() && s.charAt(counter) != ' ') {
                sb.append(s.charAt(counter));
                counter++;
            }
            if (result.containsKey(pattern.charAt(i)) && !Objects.equals(result.get(pattern.charAt(i)), sb.toString())) {
                return false;
            }
            if (!result.containsKey(pattern.charAt(i)) && result.containsValue(sb.toString())) {
                return false;
            }
            result.put(pattern.charAt(i), sb.toString());
            counter++;
        }
        return counter >= s.length();
    }
}
