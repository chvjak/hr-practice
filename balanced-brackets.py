f = open('balanced-brackets.txt')
def input():
    return f.readline()

def is_matched(expression):
    opening = '{[('
    closing = '}])'
    matching = {')':'(', '}':'{', ']' : '['}
    bracket_stack = []
    for c in expression:
        if c in opening:
            bracket_stack.append(c)
        else:
            # c in closing
            if len(bracket_stack) and bracket_stack[-1] == matching[c]:
                bracket_stack.pop()
            else:
                return False
    else:
        if len(bracket_stack) > 0 :
            return False
        else:
            return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
