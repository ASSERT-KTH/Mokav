def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	sum = 0
	for i in range(1, (n + 1)):
	    sum += i
	m = (m % sum)
	for i in range(1, (n + 1)):
	    m -= i
	    if (m < 0):
	        m += i
	        break
	global_list.append(m)
	return global_list