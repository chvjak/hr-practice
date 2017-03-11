file = open('hackerrank-in-a-string.txt')

def input():
    return file.readline()

N = int(input().strip())

s = input().strip()

for i in range(N):

    sseq = 'hackerrank'
    ssix = 0
    for j in range(len(s)):
        if sseq[ssix] == s[j]:
            ssix += 1

            if ssix == len(sseq):
                print('YES')
                break  # found
    else:
        print('NO')


