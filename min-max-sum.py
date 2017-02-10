f = open('min-max-sum1.txt')
def input():
    return f.readline()

import sys


a,b,c,d,e = input().strip().split(' ')
nums = [int(a),int(b),int(c),int(d),int(e)]

tmp = [[nums[j] for j in range(4) if j != i] for i in range(4)]


sums = [sum([nums[j] for j in range(4) if j != i]) for i in range(4)]
res = [str(x) for x in [min(sums),max(sums)]]
print(' '.join(res))