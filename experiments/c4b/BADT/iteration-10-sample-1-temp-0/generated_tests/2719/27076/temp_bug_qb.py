def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	ans = 1
	while (a <= b):
	    a *= 3
	    b *= 2
	    ans += 1
	global_list.append(ans)
	return global_list