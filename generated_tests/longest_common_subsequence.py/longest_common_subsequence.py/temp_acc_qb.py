
def patched_func(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        return a[0] + patched_func(a[1:], b[1:])

    else:
        return max(
            patched_func(a, b[1:]),
            patched_func(a[1:], b),
            key=len
        )

