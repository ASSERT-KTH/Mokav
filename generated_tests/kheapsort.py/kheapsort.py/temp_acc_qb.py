
def patched_func(arr, k):
    return_list = []
    import heapq

    heap = arr[:k]
    heapq.heapify(heap)

    for x in arr[k:]:
        return_list.append(heapq.heappushpop(heap, x))

    while heap:
        return_list.append(heapq.heappop(heap))

    return return_list