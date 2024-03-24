def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	count = 0
	for a in range(0, (max(n, m) + 1)):
	    for b in range(0, (max(n, m) + 1)):
	        if ((((a * a) + b) == n) and ((a + (b * b)) == m)):
	            count = (count + 1)
	ret_values.append(count)

	return ret_values
