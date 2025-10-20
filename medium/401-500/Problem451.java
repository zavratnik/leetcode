import java.util.*;

public class Problem451 {

    public static void main(String[] args) {
        String s = "tree";
        Problem451 solution = new Problem451();

        String result = solution.frequencySort(s);
        System.out.println(result); // "eetr" or "eert"
    }

    public String frequencySort(String s) {
        HashMap<Character, Integer> mapa = new HashMap<>();

        for (char sil : s.toCharArray()) {
            mapa.merge(sil, 1, Integer::sum);
        }

        List<Character> znaki = new ArrayList<>(mapa.keySet());
        znaki.sort((a, b) -> mapa.get(b) - mapa.get(a));

        StringBuilder sb = new StringBuilder();
        for (char znak : znaki) {
            int k = mapa.get(znak);
            sb.append(String.valueOf(znak).repeat(k));
        }

        return sb.toString();
    }
}
