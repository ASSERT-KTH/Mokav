def original_func(*args):
	global_list = []
	
	(x, y) = map(int, args[0].split())
	n = max(x, y)
	m = min(x, y)
	res = 0
	if (((n % 10) != 0) and ((m % 10) != 0)):
	    for i in range(1, ((n % 10) + 1)):
	        for j in range(1, ((m % 10) + 1)):
	            if (((i + j) % 5) == 0):
	                res += 1
	    global_list.append((((((n // 10) * 2) * m) + ((((m // 10) * 2) * n) % 10)) + res))
	elif ((n % 10) == 0):
	    global_list.append((((m * 2) * n) // 10))
	elif ((m % 10) == 0):
	    global_list.append((((n * 2) * m) // 10))
	return global_list