
def patched_func(arr):
    for x in arr:
        if isinstance(x, list):
            for y in patched_func(x):
                yield y
        else:
            yield x

