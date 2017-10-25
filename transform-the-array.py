f = open('transform-the-array.txt')
def input():
    return f.readline()

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    numbers = [int(x) for x in input().strip().split(' ')]

    i1 = 0
    while True:
        while i1 < N - 1 and numbers[i1] == 0 :
            i1 += 1

        if i1 == N - 1:
            break

        i2 = i1 + 1

        while i2 < N and numbers[i2] == 0 :
            i2 += 1

        if i2 == N:
            break

        if numbers[i1] == numbers[i2]:
            numbers[i1] *= 2
            numbers[i2] = 0
        else:
            i1 += 1
            i2 += 1


    i1 = 0
    while i1 < N and numbers[i1] != 0:
        i1 += 1

    i2 = i1
    while True:
        while i1 < N and numbers[i1] == 0:
            i1 += 1
        if i1 == N:
            break

        numbers[i2] = numbers[i1]
        numbers[i1] = 0
        i2 += 1

    print(numbers)

