def MaximalSquare(board):
    N = len(board)
    h_ones = [[0] * N for i in range(N)]
    v_ones = [[0] * N for i in range(N)]
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            if v == '1':
                if c == 0:
                    h_ones[r][c] = 1
                else:
                    h_ones[r][c] = h_ones[r][c - 1] + 1

                if r == 0:
                    v_ones[r][c] = 1
                else:
                    v_ones[r][c] = v_ones[r - 1][c] + 1

    max_square_side = -1
    for r in reversed(range(N)):
        for c in reversed(range(N)):
            square_side = min(h_ones[r][c], v_ones[r][c])
            for i in range(min(h_ones[r][c], v_ones[r][c])):
                if square_side - i > min(h_ones[r - i][c - i], v_ones[r - i][c - i]):
                    square_side = i
                    break

            max_square_side = max(max_square_side, square_side)

    return max_square_side * max_square_side


# keep this function call here
print(MaximalSquare(["0111", "1101", "0111"]))

















