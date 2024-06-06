
def patched_func(a, b, k):
    if k == 0:
        return [[]]

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in patched_func(i + 1, b, k - 1)
        )

    return ret

