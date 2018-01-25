import sys
def max_sum_subarray(array):
    N = len(array)
    if N == 0:
        return 0, []
    max_sum = -sys.maxsize
    current_sum = 0
    si = ei = 0
    cssi = 0
    for i in range(N):
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
            si = cssi
            ei = i

        if current_sum < 0:
            current_sum = 0
            cssi = i + 1

    return max_sum, array[si:ei+1]


print(max_sum_subarray([]))
print(max_sum_subarray([-1]))
print(max_sum_subarray([0]))
print(max_sum_subarray([1]))
print(max_sum_subarray([5, -1,2]))