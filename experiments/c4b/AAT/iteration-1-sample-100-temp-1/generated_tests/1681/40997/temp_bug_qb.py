def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	count = 0
	for a in range(0, max(n, m)):
	    for b in range(0, max(n, m)):
	        if ((((a ** 2) + b) == n) and ((a + (b ** 2)) == m)):
	            count = (count + 1)
	global_list.append(count)
	return global_list