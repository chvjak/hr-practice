def partition(arr):
    pivot = arr[0]

    l_arr = []
    r_arr = []

    for v in arr[1:]:
        if v < pivot:
            l_arr.append(v)
        else:
            r_arr.append(v)

    return l_arr, pivot, r_arr


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    l_arr, pivot, r_arr = partition(arr)

    l_arr = quick_sort(l_arr)
    r_arr = quick_sort(r_arr)

    return l_arr + [pivot] + r_arr


'''
f = open('quick_sort_list1.txt')
l = f.readline()
nums = [int(x) for x in l.strip().split(',')]
print(len(nums))
'''
N = 30000
nums = [0] * N
import random
for i in range(N):
    nums[i] = random.randint(0, 3)

#print(quick_sort([3, 1, 2]))
#print(quick_sort([3, 1, 2, 4, 6, 5]))
import sys
sys.setrecursionlimit(N)
print(quick_sort(nums[:N]))
