def original_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split(' '))
	for i in range(1, (n + 1)):
	    if (((i * (i + 1)) // 2) > m):
	        m -= ((i * (i - 1)) // 2)
	        global_list.append(m)
	        break
	return global_list