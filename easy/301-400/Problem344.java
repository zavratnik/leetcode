import java.util.*;

public class Problem344 {

    public static void main(String[] args) {
        char[] s = {'h', 'e', 'l', 'l', 'o'};
        Problem344 solution = new Problem344();

        solution.reverseString(s);
        System.out.println(Arrays.toString(s)); // [o, l, l, e, h]
    }

    public void reverseString(char[] s) {
        int left = 0;
        int right = s.length - 1;

        while (left < right) {
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            left++;
            right--;
        }
    }
}
