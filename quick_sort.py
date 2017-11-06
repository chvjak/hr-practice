def partition(arr):
    N = len(arr)
    pivot = arr[0]

    l_ix = 1
    r_ix = N - 1

    while l_ix < r_ix:
        while arr[l_ix] < pivot:
            l_ix += 1

        while arr[r_ix] > pivot:
            r_ix -= 1

        if arr[l_ix] > arr[r_ix]:
            arr[l_ix], arr[r_ix] = arr[r_ix], arr[l_ix]

            #l_ix += 1
            #r_ix -= 1

    # l_ix == r_ix => swap arr[l_ix] with arr[0] = pivot, return l_ix
    arr[l_ix], arr[0] = arr[0], arr[l_ix]

    return l_ix


def quick_sort(arr):
    N = len(arr)
    if N < 2:
        return arr

    pivot_ix = partition(arr)

    l_arr = quick_sort(arr[:pivot_ix])
    r_arr = quick_sort(arr[pivot_ix + 1:])

    return l_arr + [arr[pivot_ix]] + r_arr


# TODO: finish
print(quick_sort([3, 4, 5, 1, 2]))