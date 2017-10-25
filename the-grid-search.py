f = open('the-grid-search.txt')
def input():
    return f.readline()

def read_grid():
    R, C = [int(x) for x in input().strip().split(' ')]

    string_list = [None] * R
    for j in range(R):
        string_list[j] = input().strip()

    return string_list


def is_grid_in_grid(needle, hs):
    hs_i1 = 0
    ix = 0
    while True:
        while hs_i1 + len(needle) - 1 < len(hs) and hs[hs_i1].find(needle[0], ix) == -1:
            hs_i1 += 1
            ix = 0

        if hs_i1 + len(needle) - 1 == len(hs):
            return False

        ix = hs[hs_i1].find(needle[0], ix)

        n_i = 1
        hs_i = hs_i1 + 1
        while n_i < len(needle) and hs_i < len(hs) and hs[hs_i][ix:ix+len(needle[0])] == needle[n_i]:
            n_i += 1
            hs_i += 1

        if n_i == len(needle):
            return True
        else:
            ix += 1


T = int(input().strip())

for i in range(T):

    hs = read_grid()
    needle = read_grid()

    if is_grid_in_grid(needle, hs):
        print("YES")
    else:
        print("NO")