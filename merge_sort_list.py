def print_list(head):
    cur = head
    res = []
    while cur != None:
        res.append(str(cur.val))
        cur = cur.next

    print(' '.join(res))


def get_len(head):
    cntr = 0
    cur = head
    while cur is not None:
        cur = cur.next
        cntr += 1

    return cntr


def get_mid(head):
    N = get_len(head)

    cntr = 1
    cur = head
    while cntr < N // 2:
        cur = cur.next
        cntr += 1

    return cur

def merge(sll, srl):
    res_list = None
    res_list_head = None
    while sll is not None and srl is not None:
        if sll.val < srl.val:
            if res_list is not None:
                res_list.next = sll

            res_list = sll
            if res_list_head is None:
                res_list_head = res_list

            sll = sll.next

        else:
            if res_list is not None:
                res_list.next = srl

            res_list = srl
            if res_list_head is None:
                res_list_head = res_list


            srl = srl.next

    if sll is not None:
        res_list.next = sll
    else:
        res_list.next = srl

    return res_list_head


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head


        mid = get_mid(head) # O(N)
        rhead = mid.next
        mid.next = None

        sll = self.sortList(head)
        srl = self.sortList(rhead)

        shead = merge(sll, srl)


        return shead

S = Solution()

f = open('quick_sort_list1.txt')
l = f.readline()
nums = [int(x) for x in l.strip().split(',')]
print(len(nums))
N = len(nums)

'''
N = 6
nums = [0] * N
import random
for i in range(N):
    nums[i] = random.randint(0, N)
'''

class ListItem:
    def __init__(self, val):
        self.val = val
        self.next = None

head = ListItem(nums[0])
cur = head
for n in nums[0:N]:
    cur.next = ListItem(n)
    cur = cur.next

print(nums)

sl = S.sortList(head)
print_list(sl)