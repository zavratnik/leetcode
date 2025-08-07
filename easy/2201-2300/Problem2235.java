public class Problem2235 {

    public static void main(String[] args) {
        int num1 = 12;
        int num2 = 5;
        Problem2235 solution = new Problem2235();

        int result = solution.sum(num1, num2);
        System.out.println(result); // 17
    }

    public int sum(int num1, int num2) {
        return num1 + num2;
    }
}
