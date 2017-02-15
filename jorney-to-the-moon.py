#Jorney to the Moon
class QuickUF:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range(n)]

    def find(self, p):
        if (p != self.parent[p]):
            self.parent[p] = self.find(self.parent[p])

        return self.parent[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if (rootP == rootQ):
            return

        if self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        elif self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1


def read_data():
    N, I = [int(x) for x in input().strip().split(' ')]
    pairs = []
    for i in range(I):
        pairs += [[int(x) for x in input().strip().split(' ')]]

    return N, pairs

def read_data2():
    f = open('journey-to-the-moon.txt')
    N, I = [int(x) for x in f.readline().strip().split(' ')]
    pairs = []
    for i in range(I):
        pairs += [[int(x) for x in f.readline().strip().split(' ')]]

    return N, pairs

N, pairs = read_data2()
connections = QuickUF(N)
for a, b in pairs:
    connections.union(a, b)

spacemen_per_country = [0] * N

for i in range(N):
    country_id = connections.find(i)
    spacemen_per_country[country_id] += 1

C = len(spacemen_per_country)
total = sum(spacemen_per_country)
res = 0

for i in range(C):
        total -= spacemen_per_country[i]
        res += spacemen_per_country[i] * total

print(res)




