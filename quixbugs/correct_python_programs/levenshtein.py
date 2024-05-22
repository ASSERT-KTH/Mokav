
def patched_func(source, target):
    if source == '' or target == '':
        return len(source) or len(target)

    elif source[0] == target[0]:
        return patched_func(source[1:], target[1:])

    else:
        return 1 + min(
            patched_func(source,     target[1:]),
            patched_func(source[1:], target[1:]),
            patched_func(source[1:], target)
        )

