class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (char[] row : board) {
            Set<Integer> nums = new HashSet<Integer>();
            for (char c : row) {
                if (c != '.' && nums.contains(c - '0')) {
                    return false;
                }
                nums.add(c - '0');
            }
        }
        for (int i = 0; i < 9; i++) {
            Set<Integer> nums = new HashSet<Integer>();
            for (int j = 0; j < 9; j++) {
                int num = board[j][i] ;
                if (num != '.' && nums.contains(num- '0')) {
                    return false;
                }
                nums.add(num- '0');
            }
            System.out.println(nums.toString());
        }
        for (int i = 1; i <=9 ; i ++) {
            int rowbase = 0;
            int colbase = 0;

            if (i > 6) {
                rowbase = 6;
            } else if (i > 3) {
                rowbase = 3;
            }
            
            if (i%3 == 0) {
                colbase = 6;
            } else if (i%3 == 2) {
                colbase = 3;
            }

            Set<Integer> nums = new HashSet<Integer>();
            for (int ii = rowbase; ii < rowbase + 3; ii++) {
                for (int jj = colbase; jj < colbase + 3; jj++) {
                    int num = board[ii][jj];
                    if (num != '.' && nums.contains(num- '0')) {
                        return false;
                    }
                    nums.add(num- '0');
                }
            }
        }
        return true;
    }
}