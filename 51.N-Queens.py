class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        queens = [-1] * n
        res = []
        row = column = 0
        while row < n:
            while column < n:
                if self.check(row, column, queens):
                    queens[row] = column
                    column = 0
                    break
                else:
                    column += 1
            if queens[row] == -1:  # no solution at current row ,we need back track
                if row == 0:
                    break
                else:
                    row -= 1
                    column = queens[row] + 1
                    queens[row] = -1
                    continue
            if row == n - 1:  # find a solution
                res.append(self.convert_res(queens))
                column = queens[row] + 1
                queens[row] = -1
                continue
            row += 1

        return res

    def convert_res (self, queen):
        board = [[ '.' for i in range(len(queen))] for i in range(len(queen))]

        for i in range(len(queen)):
            board[i][queen[i]] = 'Q'
        for i in range(len(queen)):
            board[i] = ''.join(board[i])
        return board

    def check (self, i, j, queen):  # ith row jth column is ok to place queen
        row = 0
        while row < i:
            if queen[row] == j or abs (i - row) == abs(j - queen[row]):
                return False
            row += 1
        return True

o = Solution()
print(o.solveNQueens(4))
print o.solveNQueens(4)