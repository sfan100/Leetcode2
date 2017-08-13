class Solution(object):
    def helper(self, target, board, row, column):
        while target and row < len(board) and column < len(board[0]):
            if row != len(board) - 1 and column < len(board[0]) - 1:  # not in last row or column
                if column == 0:  # if column == 0 , do not consider its left
                    if board[row + 1][column] != target[0] and board[row][column + 1] != target[0]:
                        return False
                    elif board[row][column + 1] != target[0]:
                        row += 1
                        target = target[1:]
                    elif board[row + 1][column] != target[0]:
                        column += 1
                        target = target[1:]
                    else:
                        return self.helper(target[1:], board, row + 1, column) or self.helper(target[1:], board, row,column + 1)
                else:
                    if board[row + 1][column] != target[0] and board[row][column + 1] != target[0] and board[row][column - 1] != target[0]:
                        return False
                    elif board[row][column + 1] != target[0] and board[row][column - 1] != target[0]:  # next row selected
                        row += 1
                        target = target[1:]

                    elif board[row + 1][column] != target[0] and board[row][column - 1] != target[0]:  # right column selected
                        column += 1
                        target = target[1:]

                    elif board[row + 1][column] != target[0] and board[row][column + 1] != target[0]:  # left column selected
                        column -= 1
                        target = target[1:]
                    else:
                        return self.helper(target[1:], board, row + 1, column) or self.helper(target[1:], board, row, column + 1) \
                            or self.helper(target[1:], board, row, column - 1)
            if row != len(board) - 1 and column == len(board[0]) - 1: # last column
                while target and column != len(board[0]) - 1:
                    if board [row][column] != target[0]:
                        return False
                    else:
                        target = target[1:]
                        column += 1
                return True if not target else False
            if row == len(board) - 1 and column != len(board[0]) - 1:  # last row
                while target and column != len(board[0]) - 1:
                    if board[row][column] != target[0]:
                        return False
                    else:
                        target = target[1:]
                        column += 1
                return True if not target else False



def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        word_l = list(word)
        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word_l[0]:
                    target = word_l[1:]
                    if self.helper(target, board, row, column):
                        return True
                    else:
                        pass
        return False



o = Solution()
print(o.exist(["ABCE","SFCS","ADEE"],"ABCCED"))