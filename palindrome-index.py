file = open('palindrome-index.txt')

def input():
    return file.readline()

T = int(input().strip())

for i in range(T):
    s = input().strip()

    sl = len(s)
    for j in range(sl // 2):
        if s[j] != s[sl - 1 - j]:
            if s[j + 1] == s[sl - 1 - j]:
                # if it is not last char to check =>...
                if j + 2 < sl // 2:
                    # check that string is still palindrome e.g ABCBBCA
                    if s[j + 2] == s[sl - 1 - j - 1]:
                        print(j)
                    else:
                        print(sl - 1 - j)   # not palindrome
                else:
                    print(j)

            else:
                print(sl - 1 - j)
            break
    else:
        print(-1)


