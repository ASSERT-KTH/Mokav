def func(*args):
	ret_values = []
	
	k = int(args[0])
	m = [int(i) for i in args[1].split()]
	m.sort()
	m = m[::(- 1)]
	months = 0
	g = 0
	if (sum(m) < k):
	    ret_values.append((- 1))
	else:
	    while (g < k):
	        g += m[months]
	        months += 1
	    ret_values.append(months)

	return ret_values
