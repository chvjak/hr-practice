def heapify(a, start, end):
    sift_down(a, start, end)

    if start > 1:
        heapify(a, start - 1, end)


def sift_down(a, root_idx, end_idx):
    if root_idx * 2 > end_idx:
        return

    left_child_idx = root_idx * 2
    right_child_idx = root_idx * 2 + 1

    max_idx = root_idx
    if left_child_idx <= end_idx and a[left_child_idx] > a[max_idx]:
        max_idx = left_child_idx

    if right_child_idx <= end_idx and a[right_child_idx] > a[max_idx]:
        max_idx = right_child_idx

    if root_idx == max_idx:
        return
    else:
        a[max_idx], a[root_idx] = a[root_idx], a[max_idx]
        sift_down(a, max_idx, end_idx)


def heap_sort(a, start, end):
    heapify(a, start, end)
    a[end], a[1] = a[1], a[end]

    if end > 1:
        heap_sort(a, start, end - 1)


a = [-1, 3, 4, 6, 1, 5, 7, 2, 8, 9]
heapify(a, len(a) - 1, len(a) - 1)
print(a)

heap_sort(a, 1, len(a) - 1)
print(a)

