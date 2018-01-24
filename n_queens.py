class Board:
    def __init__(self, N):
        self.R = self.C = N
        row = ['.'] * self.C
        self.data = [row[:] for __ in range(self.R)]
        self.pieces = []

    def __repr__(self):
        res = []
        for row in self.data:
            res.append(''.join(row))

        return '\n'.join(res)

    def to_list(self):
        res = []
        for row in self.data:
            res.append(''.join(row))

        return res

    def place_queen(self, r, c):
        self.pieces.append((r, c))
        self.data[r][c] = 'Q'

    def remove_queen(self, r, c):
        self.pieces.remove((r, c))
        self.data[r][c] = '.'

    def is_cell_safe(self, r, c):
        for pr, pc in self.pieces:
            if pr == r or pc == c or abs(pr - r) == abs(pc - c):
                return False
        else:
            return True


def place_queens(board, N, solutions):
    if N == 0:
        print(board)
        print()
        solutions.append(board.to_list())
        return

    #for r in range(board.R):
    r = N - 1
    for c in range(board.C):
        if board.is_cell_safe(r, c):
            board.place_queen(r, c)
            place_queens(board, N - 1, solutions)
            board.remove_queen(r, c)

    return


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, N):
        board = Board(N)

        solutions = []  # list of board.__repr__()
        place_queens(board, N, solutions)

        # print(len(solutions))
        # for s in solutions:
        #    print(s)

        return solutions

S = Solution()

print(S.solveNQueens(8))