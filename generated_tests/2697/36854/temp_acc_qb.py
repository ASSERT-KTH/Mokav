def patched_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	res = (- 1)
	m = max(a, b, c, d)
	for i in range(0, (m + 1)):
	    j = ((((a * i) + b) - d) // c)
	    jd = ((((a * i) + b) - d) % c)
	    if ((jd == 0) and (((a * i) + b) >= max(b, d))):
	        res = ((a * i) + b)
	        break
	global_list.append(res)
	return global_list