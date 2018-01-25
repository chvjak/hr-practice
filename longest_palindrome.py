
str1 = 'aaaabbaa'
N = len(str1)
row = [None] * (N + 1)
cache = [row[:] for x in range(N)]

for i in range(N):
    cache[i][1] = True #on every char pos there is palindrome seq of len=1
    if i < N - 1 :
        cache[i][2] = str1[i] == str1[i + 1]


for si in reversed(range(N)):
    for ps_len in range(3, N - si + 1):
        cache[si][ps_len] = cache[si + 1][ps_len - 2] and str1[si] == str1[si + ps_len - 1]
        print(si, ps_len, str1[si], str1[si + ps_len - 1], cache[si][ps_len])

for ps_len in reversed(range(1, N + 1)):
    for si in range(N):
        if cache[si][ps_len]:
            print(str1[si:si + ps_len])

