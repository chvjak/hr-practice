def is_target_sum_possible(arr, target_sum):
    N = len(arr)

    for i in range(N - 1):
        cur_sum = 0
        for j in range(i + 1, N):
            cur_sum += arr[j]
            if cur_sum == target_sum:
                return True

    return False
