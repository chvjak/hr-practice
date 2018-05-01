# Definition for singly-linked list.
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)
def print_list(head):
    cur = head
    res = []
    while cur != None:
        res.append(str(cur.val))
        cur = cur.next

    print(' '.join(res))


def append_list(head, to_append):
    cur = head
    if cur == None:
        return to_append

    while cur.next != None:
        cur = cur.next

    cur.next = to_append

    return head


def get_tail(head):
    cur = head
    if cur == None:
        return cur

    while cur.next != None:
        cur = cur.next

    return cur


def partition(head):
    cur = head
    ll = None
    rl = None

    cur = cur.next  # skip pivot
    pivot = head
    pivot.next = None

    while cur != None:
        cur_next = cur.next
        cur.next = None

        if cur.val < pivot.val:
            # starting from second element, remember the elelment added as 'tail' and append to it
            if ll is None:
                new_llt = cur
                ll = append_list(ll, new_llt)
                llt = new_llt
            else:
                new_llt = cur
                append_list(llt, new_llt)
                llt = new_llt
        else:
            if rl is None:
                new_rlt = cur
                rl = append_list(rl, new_rlt)
                rlt = new_rlt
            else:
                new_rlt = cur
                append_list(rlt, new_rlt)
                rlt = new_rlt
        cur = cur_next

    return ll, pivot, rl


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        ll, pl, rl = partition(head)

        sll = self.sortList(ll)
        srl = self.sortList(rl)

        if sll is not None:
            sll_tail = get_tail(sll)  # O(len(ssl)), but it's the same as partition
            sll_tail.next = pl
        else:
            sll = pl

        pl.next = srl

        return sll

S = Solution()

'''
f = open('quick_sort_list1.txt')
l = f.readline()
nums = [int(x) for x in l.strip().split(',')]
print(len(nums))
'''

N = 60000
nums = [0] * N
import random
for i in range(N):
    nums[i] = random.randint(0, N)


class ListItem:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListItem(nums[0])
cur = head
for n in nums[0:N]:
    cur.next = ListItem(n)
    cur = cur.next

#print_list(head)
#s_head = S.sortList(head)

import cProfile
cProfile.run('s_head = S.sortList(head)')

#print_list(s_head)