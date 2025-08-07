public class Problem13 {

    public static void main(String[] args) {
        String s = "MCMXCIV";
        Problem13 solution = new Problem13();

        int result = solution.romanToInt(s);
        System.out.println(result); // 1994
    }

    public int romanToInt(String s) {
        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int currentVal = getValue(s.charAt(i));
            if (i < n - 1 && currentVal < getValue(s.charAt(i + 1))) {
                total -= currentVal;
            } else {
                total += currentVal;
            }
        }
        return total;
    }

    private int getValue(char c) {
        switch (c) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}
