file = open('anagram.txt')

def input():
    return file.readline()


N = int(input().strip())

from collections import Counter

for i in range(N):
    s12 = input().strip()

    L = len(s12)
    if L % 2 == 1:
        print(-1)
        continue

    s1 = s12[:L // 2]
    s2 = s12[L // 2:]

    s1c = Counter(s1)
    s2c = Counter(s2)

    s1c -= s2c

    print(sum([x for x in s1c.values()]))
