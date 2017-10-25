f = open('prefix-neighbors.txt')
def input():
    return f.readline()

class Trie:
    def __init__(self):
        self.data = {}

    def add(self, s):
        cur_node = self.data
        for c in s:
            if c not in cur_node.keys():
                cur_node[c] = {}

            cur_node = cur_node[c]

        cur_node['$'] = None  # mark the node as end of the string. Consider accounting all EOSes centrally


#NOTE: benefit from subtrees could be summed independently if it is 'odd' or 'even'
def DFSX(node, string_count, benefit):
    even_benefit = odd_benefit = 0
    if '$' in node.keys():
        if string_count % 2 == 0:
            even_benefit += benefit
        else:
            odd_benefit += benefit
        string_count += 1

    for (k, v) in node.items():
        if k != '$':
            eb, ob = DFSX(v, string_count, benefit + ord(k))
            even_benefit += eb
            odd_benefit += ob

    return even_benefit, odd_benefit


N = int(input().strip())
D = input().strip().split(' ')

T = Trie()
for s in D:
    T.add(s)

max_benefit = 0

string_count = 1

for (k, node) in T.data.items():
    max_benefit += max(DFSX(node, string_count, ord(k)))

print(max_benefit)




