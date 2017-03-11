f = open('bot_saves_princess2.txt')
def input():
    return f.readline()

def displayNextMove(n, grid):
    # print all the moves here
    if len([r for r in grid if 'm' in r]) == 0:
        return ""

    if len([r for r in grid if 'p' in r]) == 0:
        return ""

    N = len(grid)
    m_pos = [(i, grid[i].index('m')) for i in range(N) if 'm' in grid[i]][0]
    p_pos = [(i, grid[i].index('p')) for i in range(N) if 'p' in grid[i]][0]

    delta_r, delta_c = m_pos[0] - p_pos[0], m_pos[1] - p_pos[1]

    v_command = []
    if delta_r != 0:
        v_command = ["UP" if delta_r > 0 else  "DOWN"]

    h_command = []
    if len(v_command) == 0:
        if delta_c != 0:
            h_command = ["LEFT" if delta_c > 0 else  "RIGHT"]

    print('\n'.join(v_command + h_command))


m = int(input())
x,y = input().strip().split(' ')
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayNextMove(m, grid)

