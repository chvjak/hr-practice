# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        cur_sorted = A
        stack = [cur_sorted]
        while cur_sorted.next is not None:
            cur_to_insert = cur_sorted.next
            while len(stack):
                maybe_smaller = stack.pop()

                if maybe_smaller.val > cur_to_insert.val:
                    greater = maybe_smaller
                    # swap

                    greater.val, cur_to_insert.val = cur_to_insert.val, greater.val
                    cur_to_insert = greater

                else:
                    stack.append(maybe_smaller)
                    break
            # restore stack
            cur_stack = cur_to_insert
            while cur_stack != cur_sorted.next:
                stack.append(cur_stack)
                cur_stack = cur_stack.next
            stack.append(cur_stack)

            cur_sorted = cur_sorted.next

        return A


l = ListNode(9)
l.next = ListNode(7)
l.next.next = ListNode(8)
l.next.next.next = ListNode(5)
S = Solution()

res = S.insertionSortList(l)


