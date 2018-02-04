class Queue:
    def __init__(self):
        self.data = []

    def enq(self, v):
        self.data.append(v)

    def deq(self):
        v = self.data[0]
        self.data.pop(0)

        return v

    def __len__(self):
        return len(self.data)


def DfsEnemyLevel(g, b, root):
    Q = Queue()
    visited = set()
    visited.add(root)

    Q.enq((0, root))

    while len(Q) > 0:
        v_level, v = Q.deq()
        for vn in g.adj[v]:

            if b.val_by_cid(vn) == '2':
                return v_level + 1

            if vn not in visited:
                Q.enq((v_level + 1, vn))


class Graph:
    def __init__(self, N):
        self.N = N
        self.adj = {i: set() for i in range(N)}

    def add_edge(self, from_v, to_v):
        self.adj[from_v].add(to_v)


class Board:
    def __init__(self, data):
        self.R = len(data)
        self.C = len(data[0])
        self.data = data

    def cell_ids(self):
        for r, row in enumerate(self.data):
            for c, v in enumerate(row):
                yield self.rc_to_cid(r, c)

    def rc_to_cid(self, r, c):
        r = r % self.R
        c = c % self.C

        return r * self.R + c

    def cid_to_rc(self, cid):
        r, c = cid // self.C, cid % self.C
        return r, c

    def neighbors(self, cid):
        r, c = self.cid_to_rc(cid)

        all_neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        return [self.rc_to_cid(*x) for x in all_neighbors]

    def val_by_cid(self, cid):
        r, c = self.cid_to_rc(cid)

        return self.data[r][c]


def ClosestEnemyII(board):
    b = Board(board)
    g = Graph(b.R * b.C)

    for cid in b.cell_ids():
        if b.val_by_cid(cid) == '1':
            root = cid
        for n in b.neighbors(cid):
            g.add_edge(cid, n)
            g.add_edge(n, cid)

    res = DfsEnemyLevel(g, b, root)

    return res


# keep this function call here
print(ClosestEnemyII(["0000", "1000", "0002", "0002"]))
















