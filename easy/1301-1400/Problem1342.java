public class Problem1342 {

    public static void main(String[] args) {
        int num = 14;
        Problem1342 solution = new Problem1342();

        int result = solution.numberOfSteps(num);
        System.out.println(result); // 6
    }

    public int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            if (num % 2 == 0) {
                num = num / 2;
                steps += 1;
            } else {
                num -= 1;
                steps += 1;
            }
        }
        return steps;
    }
}
