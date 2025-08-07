import java.util.*;

public class Problem54 {

    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        Problem54 solution = new Problem54();

        List<Integer> result = solution.spiralOrder(matrix);
        System.out.println(result); // [1, 2, 3, 6, 9, 8, 7, 4, 5]
    }

    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;

        int zgoraj = 0;
        int spodaj = m - 1;
        int levo = 0;
        int desno = n - 1;

        int direction = 0;

        List<Integer> result = new ArrayList<Integer>();

        while (zgoraj <= spodaj && levo <= desno) {
            if (direction == 0) {
                for (int i = levo; i <= desno; i++) {
                    result.add(matrix[zgoraj][i]);
                }
                zgoraj++;
                for (int j = zgoraj; j <= spodaj; j++) {
                    result.add(matrix[j][desno]);
                }
                desno--;
                direction = 1;
            } else {
                for (int p = desno; p >= levo; p--) {
                    result.add(matrix[spodaj][p]);
                }
                spodaj--;
                for (int q = spodaj; q >= zgoraj; q--) {
                    result.add(matrix[q][levo]);
                }
                levo++;
                direction = 0;
            }
        }

        return result;
    }
}
