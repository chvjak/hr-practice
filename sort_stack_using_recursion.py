class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0


def get_max(stack1, max1):
    if stack1.is_empty():
        return max1

    tmp = stack1.pop()
    max1 = get_max(stack1, max(tmp, max1))

    if tmp != max1:
        stack1.push(tmp)

    return max1

def sort_stack(stack1):
    if stack1.is_empty():
        return

    max1 = get_max(stack1, 0)

    sort_stack(stack1)
    stack1.push(max1)


s = Stack()
s.push(5)
s.push(2)
s.push(3)
s.push(1)

sort_stack(s)

print(s.data)


