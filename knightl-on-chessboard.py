
MAX_INT = 10 ** 10

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, m):
        return Position(self.x + m[0], self.y + m[1])

    def __eq__(self, m):
        return self.x == m[0] and self.y == m[1]


def valid_pos(pos):
    if 0 <= pos.x < N and 0 <= pos.y < N:
        return True
    else:
        return False


def available_moves(pos):
    all_moves = [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (-b, a), (b, -a), (-b, -a)]
    return [m for m in all_moves if valid_pos(pos + m)]


def get_min_moves(pos):
    cached = cache[pos.x][pos.y]
    if cached is not None and cached != -1:
        return cached

    cache[pos.x][pos.y] = -1   #being visited

    if pos == (N - 1, N - 1):
        return 0
    else:
        res = MAX_INT

        am = available_moves(pos)
        for m in am:
            new_pos = pos + m
            if cache[new_pos.x][new_pos.y] != -1:  # to void loops don't step on those being visited
                moves_to_NN = 1 + get_min_moves(new_pos)

                if moves_to_NN < res:
                    res = moves_to_NN

        if res == MAX_INT:
            cache[pos.x][pos.y] = None  # at least unmark  'being visited'
        else:
            cache[pos.x][pos.y] = res
        return res

def put_min_moves(pos, move_count):
        if pos == (0, 0):
            return
        else:
            am = available_moves(pos)
            for m in am:
                new_pos = pos + m
                if cache[new_pos.x][new_pos.y] is None or cache[new_pos.x][new_pos.y] > move_count + 1:
                    cache[new_pos.x][new_pos.y] = move_count + 1

                    put_min_moves(new_pos, move_count + 1)


            return



#N = int(input().strip())
N = 7
rt = [None] * (N - 1)
res = []
for j in range(N - 1):
    res.append(rt[:])

for a in range(1, N):
    for b in range(a, N):

        rt = [None] * N
        cache = []
        for j in range(N):
            cache.append(rt[:])

        #res[a - 1][b - 1] = get_min_moves(Position(0, 0))

        put_min_moves(Position(N - 1, N - 1), 0)
        res[a - 1][b - 1] = cache[0][0]
        res[b - 1][a - 1] = res[a - 1][b - 1]

for r in res:
    print(' '.join([str(x) if x != MAX_INT else '-1' for x in r]))