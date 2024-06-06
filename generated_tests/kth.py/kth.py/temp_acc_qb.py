
def patched_func(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return patched_func(below, k)
    elif k >= num_lessoreq:
        return patched_func(above, k - num_lessoreq)
    else:
        return pivot
