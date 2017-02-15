f = open('bot_clean.txt')
def input():
    return f.readline()

def getNextMove(r, c, grid):
    # print all the moves here

    if len([r for r in grid if 'd' in r]) == 0:
        return ""

    N = len(grid)
    m_pos = (r, c)
    g_pos = [(i, grid[i].index('d')) for i in range(N) if 'd' in grid[i]]

    deltas_rc = [(m_pos[0] - g_r, m_pos[1] - g_c) for (g_r, g_c) in g_pos]
    deltas_rc.sort(key=lambda delta: abs(delta[0]) + abs(delta[1]))

    delta_r, delta_c = deltas_rc[0]


    res = ""
    if delta_r == 0 and delta_c == 0:
        res = "CLEAN"
    elif delta_r != 0:
        res = "UP" if delta_r > 0 else  "DOWN"
    else:
        res = "LEFT" if delta_c > 0 else  "RIGHT"

    return res


m = 5
x, y = [int(x) for x in input().strip().split(' ')]
grid = []
for i in range(0, m):
    grid.append(input().strip())

print(getNextMove(x, y, grid))