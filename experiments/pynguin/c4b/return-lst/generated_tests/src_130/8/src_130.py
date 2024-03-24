def func(*args):
	ret_values = []
	
	'input\n2 4 5\n'
	(l, r, k) = map(int, args[0].split())
	t = 0
	for x in range(100000):
	    if (((k ** x) >= l) and ((k ** x) <= r)):
	        ret_values.append((k ** x), end=' ')
	        t = 1
	    elif ((k ** x) > r):
	        break
	if (t == 0):
	    ret_values.append((- 1))

	return ret_values
