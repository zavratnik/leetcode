import java.util.*;

public class Problem49 {

    public static void main(String[] args) {
        String[] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
        Problem49 solution = new Problem49();

        List<List<String>> result = solution.groupAnagrams(strs);
        System.out.println(result); // [[eat, tea, ate], [tan, nat], [bat]]
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mapa = new HashMap<>();

        for (String str : strs) {
            int[] frekvence = new int[26];
            for (int i = 0; i < str.length(); i++) {
                char c = str.charAt(i);
                frekvence[c - 'a']++;
            }

            String key = Arrays.toString(frekvence);

            mapa.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
        }
        return new ArrayList<>(mapa.values());
    }
}
