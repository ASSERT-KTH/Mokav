def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (y, k, n) = str(args[0]).split()
	    y = int(y)
	    k = int(k)
	    n = int(n)
	    res = list()
	    head = (y // k)
	    tail = (n // k)
	    for i in range(head, (tail + 1)):
	        v = (i * k)
	        if (y < v <= n):
	            res.append(str((v - y)))
	    if (len(res) > 0):
	        ret_values.append(' '.join(res))
	    else:
	        ret_values.append((- 1))

	return ret_values
