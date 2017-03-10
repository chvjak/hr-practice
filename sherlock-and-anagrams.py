file = open('sherlock-and-anagrams.txt')

def input():
    return file.readline()

def CNK(N, K):
    # N! / (N-K)! / K! =
    # PROD(1..N) / PROD(1..N-K) / PROD(1..K) =
    # PROD(K+1..N) / PROD(1..N-K) = for big K, K=48 : 49 * 50 / 1 * 2
    # PROD(N-K+1..N) / PROD(1..K) = for small K, e.g K=2 : 50 * 49 / 1 * 2

    if N == K:
        return 1

    nom = 1
    denom = 1

    for i in range(max(N - K + 1, K + 1), N + 1):
        nom *= i

    for i in range(1, min(N - K, K) + 1):
        denom *= i

    return nom / denom


T = int(input().strip())

from collections import Counter

for i in range(T):
    s = input().strip()
    sc = Counter(s)

    ccgt1 = [cc for cc in sc.values() if cc > 1]  # char counts, > 1
    L = len(ccgt1)
    count_agp1 = [0] * L  # num of anagram pairs of same char for each char with count > 1
    for cci in range(L):
        cc = ccgt1[cci]
        for i in range(1, cc // 2 + 1):
            count_agp1[cci] += CNK(cc, i * 2)

    res = sum(count_agp1)
    from itertools import combinations

    for i in range(2, L + 1):
        for p in combinations(range(L), i):
            prod = 1
            for m in [count_agp1[i] for i in p]:
                prod *= m
            res += 2 * prod

    print(res)




