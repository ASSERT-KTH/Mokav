
def patched_func(a, b):
    if b == 0:
        return a
    else:
        return patched_func(b, a % b)