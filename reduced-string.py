f = open('reduced-string1.txt')
def input():
    return f.readline()

s = input()

i = 0
while i + 1 < len(s):
    if s[i] == s[i + 1]:
        spfx = ''
        if i - 1 >= 0:
            spfx = s[:i]

        ssfx = ''
        if i + 2 < len(s):
            ssfx = s[i + 2:]

        s = spfx + ssfx

        if i - 1 >= 0:
            i -= 1
    else:
        i += 1

print(s)