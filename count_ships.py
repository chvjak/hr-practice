class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        res = 0
        for r, row in enumerate(board):
            val_prev = None
            for c, val in enumerate(row):
                if val == 'X':
                    if val_prev == '.' or val_prev is None:
                        if r == 0 or board[r - 1][c] == '.':
                            res += 1

                val_prev = val

        return res




S = Solution()
print(S.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))

