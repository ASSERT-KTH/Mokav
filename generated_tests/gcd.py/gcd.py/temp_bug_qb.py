def original_func(a,b):
    if b==0:
        return a
    else:
        return original_func(a,a%b)