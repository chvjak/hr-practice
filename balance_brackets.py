class Stack:
    def __init__(self):
        self.data = []

    def push(self, c):
        self.data.append(c)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return 0 == len(self.data)


def is_balanced(expr1):
    S = Stack()
    openining = '[{('
    closing = ']})'
    matching = {'(':')', ')':'(', '[':']', ']':'[', '{': '}', '}': '{'}

    res = ''
    for c in expr1:
        if c in openining:
            S.push(c)
        else:
            while not S.is_empty() and S.top() != matching[c]:          # {[{{( + ] => {[] + }
                S.pop()         # those on stack MIGHT be invalid

            if not S.is_empty():
                S.pop()         # VALID pair is found, pop matching opening
            else:
                return False    # Current bracket is INVALID

    if S.is_empty():
        return True
    else:
        return False            # those on stack are INVALID

# TODO: Solve some
# ambiguity in the task:
# '([[[)]]] -> balanced = () OR balanced = [[[]]]
# 'greedy' balancing VS 'min drop' balancing
# there is also 'min reverse' balancing: }}}{ -> balanced: {}{}

def balance(expr1):
    ...


print(is_balanced('[{()}]()'))
print(is_balanced('[{()}](]'))
print(is_balanced('[(])'))
print(is_balanced('[](){}'))
print(is_balanced('())'))
print(is_balanced('[())]'))
print(is_balanced('[())]'))

#[[[}]]]

