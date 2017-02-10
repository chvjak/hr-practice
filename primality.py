f = open('primapity1.txt')
def input():
    return f.readline()

N = int(input())

for i in range(N):
    a = int(input())

    if a == 1:
        print ("Not prime")
    else:
        from math import sqrt
        for j in range(2, int(sqrt(a) + 1)):
            if a % j == 0:
                print ("Not prime")
                break
        else:
            print ("Prime")