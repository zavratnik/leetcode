import java.math.BigInteger;

public class Problem67 {

    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";
        Problem67 solution = new Problem67();

        String result = solution.addBinary(a, b);
        System.out.println(result); // 10101
    }

    public String addBinary(String a, String b) {
        BigInteger i = new BigInteger(a, 2);
        BigInteger j = new BigInteger(b, 2);

        BigInteger result = i.add(j);

        return result.toString(2);
    }
}
