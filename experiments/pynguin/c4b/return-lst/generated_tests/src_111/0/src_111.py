def func(*args):
	ret_values = []
	
	(y, k, n) = [int(i) for i in args[0].split()]
	a = (y % k)
	m = []
	for i in range(n):
	    h = ((i * k) - a)
	    num = (h + y)
	    if (num <= n):
	        if (h > 0):
	            m.append(h)
	    else:
	        break
	if (len(m) > 0):
	    ret_values.append(*m)
	else:
	    ret_values.append((- 1))

	return ret_values
