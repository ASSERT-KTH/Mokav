def original_func(height, start=1, end=3):
    steps = []
    if height > 0:
        helper = ({1, 2, 3} - {start} - {end}).pop()
        steps.extend(original_func(height - 1, start, helper))
        steps.append((start, helper))
        steps.extend(original_func(height - 1, helper, end))

    return steps