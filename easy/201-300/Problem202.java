import java.util.*;

public class Problem202 {

    public static void main(String[] args) {
        int n = 19;
        Problem202 solution = new Problem202();

        boolean result = solution.isHappy(n);
        System.out.println(result); // true
    }

    public boolean isHappy(int n) {
        Map<Integer, Integer> stevilo = new HashMap<>();
        List<Integer> stevilo_zmes = new ArrayList<>();

        while (n != 1) {
            int temp = 0;

            while (n > 0) {
                stevilo_zmes.add(n % 10);
                n = n / 10;
            }
            while (!(stevilo_zmes.isEmpty())) {
                int temp_znotraj = stevilo_zmes.get(0);
                temp_znotraj = temp_znotraj * temp_znotraj;
                temp += temp_znotraj;
                stevilo_zmes.remove(0);
            }

            n = temp;

            if (!(stevilo.containsKey(n))) {
                stevilo.put(n, 1);
            } else {
                return false;
            }
        }
        return true;
    }
}
