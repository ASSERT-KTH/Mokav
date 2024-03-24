def func(*args):
	ret_values = []
	
	(y, k, n) = map(int, args[0].split())
	x = k
	lst = []
	while (x <= n):
	    if (x > y):
	        lst.append((x - y))
	    x += k
	if (len(lst) < 1):
	    ret_values.append((- 1))
	else:
	    lst.sort()
	    for ans in lst:
	        ret_values.append(ans, end=' ')

	return ret_values
