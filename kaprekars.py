def KaprekarsConstant(num):
    lnum = list(str(num))
    while len(lnum) < 4:
        lnum.insert(0, '0')

    snum = lnum
    snum.sort()
    num2 = int(''.join(snum))

    snum.sort(reverse=True)
    num1 = int(''.join(snum))

    if num1 - num2 == 6174:
        # code goes here
        return 1
    else:
        return 1 + KaprekarsConstant(num1 - num2)


# keep this function call here

print(KaprekarsConstant(2111))