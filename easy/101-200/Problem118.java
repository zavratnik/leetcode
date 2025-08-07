import java.util.*;

public class Problem118 {

    public static void main(String[] args) {
        int numRows = 5;
        Problem118 solution = new Problem118();

        List<List<Integer>> result = solution.generate(numRows);
        System.out.println(result); // [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    }

    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();
        int counter = 1;

        for (int i = 1; i <= numRows; i++) {
            List<Integer> middleman = new ArrayList<Integer>();
            if (i < 3) {
                for (int j = 0; j < i; j++) {
                    middleman.add(1);
                }
                temp = middleman;
                counter++;
            } else {
                for (int p = 0; p < counter; p++) {
                    if (p == 0 || p == counter - 1) {
                        middleman.add(1);
                    } else {
                        int vmesna = temp.get(p - 1) + temp.get(p);
                        middleman.add(vmesna);
                    }
                }
                temp = middleman;
                counter++;
            }
            result.add(temp);
        }

        return result;
    }
}
