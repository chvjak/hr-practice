f = open('sherlock-and-gcd.txt')
def input():
    return f.readline()

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def is_prime(a):
    for i in range(2, int(a ** 0.5)):
        if a % i == 0:
            return False
    else:
        return True


def is_there_mut_prime(A):
    N = len(A)

    # if there is 1 or prime in A
    #for ai in A:
    #   if is_prime(ai) or ai == 1:
    #      return True

    # OR if there is mutually prime pair
    for i in range(N - 1):
        for j in range(i + 1, N):
            #print(A[i], A[j], gcd(A[i], A[j]))
            if gcd(A[i], A[j]) == 1:
                return True

    return False


T = int(input())
for t in range(T):
    N = int(input())
    A = [int(x) for x in input().strip().split(' ')]

    if is_there_mut_prime(A):
        print('YES')
    else:
        print('NO')

