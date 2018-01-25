class Stack:
    def __init__(self):
        self.data = []

    def push(self, v):
        self.data.append(v)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        res = 0  # volume
        hs = Stack()
        ws = Stack()
        for i, h in enumerate(A):
            if hs.is_empty() or h < hs.top():
                hs.push(h)
                ws.push(i)
                h_prev = 0

            else:
                while not hs.is_empty():
                    h0 = hs.pop()
                    w0 = ws.pop()
                    res += (i - w0 - 1) * (min(h, h0) - h_prev)
                    h_prev = min(h, h0)

                    if h0 >= h:
                        hs.push(h0)
                        ws.push(w0)

                        hs.push(h)
                        ws.push(i)
                        h_prev = 0
                        break
                else:
                    hs.push(h)
                    ws.push(i)
                    h_prev = 0

        return res


S = Solution()

print(S.trap([0,1,0,2,0,1]))    #2
print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))    #6
print(S.trap([6,4,1,0,6]))      # 13
print(S.trap([7,4,1,0,6,7]))      # 13 + 4
print(S.trap([7,4,1,0,6,7,2,3]))      # 13 + 4 + 1
print(S.trap([7,4,1,0,6,7,0,3]))      # 13 + 4 + 3

print(S.trap([8,4,1,0,6,7,0,3]))      # 20 expected, 16 returned
