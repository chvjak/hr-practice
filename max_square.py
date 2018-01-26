def update_ms(max_square, h_ones, v_ones, r, c):
    max_square[r][c] = min(h_ones[r][c], v_ones[r][c], r + 1, c + 1)

    if r > 0 and c > 0:
        max_square[r][c] = min(max_square[r][c], max_square[r - 1][c - 1] + 1)

def MaximalSquare(board):
    R = len(board)
    C = len(board[0])
    h_ones = [[0] * C for i in range(R)]
    v_ones = [[0] * C for i in range(R)]
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
    max_square = [[0] * C for i in range(R)]


    for r0 in range(R):
        c = 0
        for r in range(r0, R):
            update_ms(max_square, h_ones, v_ones, r, c)

            max_square_side = max(max_square_side, max_square[r][c])

            c = (c + 1) % C

    for c0 in range(C):
        r = 0

        for c in range(c0, C):

            update_ms(max_square, h_ones, v_ones, r, c)

            max_square_side = max(max_square_side, max_square[r][c])

            r = (r + 1) % R


    return max_square_side * max_square_side


# keep this function call here
#print(MaximalSquare(["0111", "1101", "0111"]))
print(MaximalSquare(["101101", "111111", "010111", "111111"]))

















