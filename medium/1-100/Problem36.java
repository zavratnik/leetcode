import java.util.*;

public class Problem36 {

    public static void main(String[] args) {
        char[][] board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        Problem36 solution = new Problem36();

        boolean result = solution.isValidSudoku(board);
        System.out.println(result); // true
    }

    public boolean isValidSudoku(char[][] board) {
        int length = board.length;

        for (int i = 0; i < length; i++) {
            Set<Character> frekvenca_horizontala = new HashSet<>();
            Set<Character> frekvenca_vertikala = new HashSet<>();

            for (int j = 0; j < length; j++) {
                char row = board[i][j];
                char cell = board[j][i];

                if (row != '.' && !frekvenca_horizontala.add(row)) {
                    return false;
                }
                if (cell != '.' && !frekvenca_vertikala.add(cell)) {
                    return false;
                }
            }
        }
        for (int startRow = 0; startRow < 9; startRow += 3) {
            for (int startCol = 0; startCol < 9; startCol += 3) {
                Set<Character> frekvenca_kvadrat = new HashSet<>();
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        char vrednost = board[startRow + i][startCol + j];
                        if (vrednost != '.' && frekvenca_kvadrat.contains(vrednost)) {
                            return false;
                        } else {
                            frekvenca_kvadrat.add(vrednost);
                        }
                    }
                }
            }
        }
        return true;
    }
}
