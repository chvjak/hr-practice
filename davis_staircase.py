f = open('davis_staircase1.txt')
def input():
    return f.readline()

def count_ways(height, cache):
    if height == 0:
        return 1

    if cache[height - 1] is not None:
        return cache[height - 1]

    res = 0
    for step in [1, 2, 3]:
        if height - step >= 0:
            res += count_ways(height - step, cache)

    cache[height - 1] = res
    return res


N = int(input().strip())
stair_heights = []
for i in range(N):
    staircase_height = int(input().strip())
    cache = [None for _ in range(staircase_height)]
    res = count_ways(staircase_height, cache)


    print(res)