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

print(quick_sort([3, 1, 2]))
print(quick_sort([3, 1, 2, 4, 6, 5]))