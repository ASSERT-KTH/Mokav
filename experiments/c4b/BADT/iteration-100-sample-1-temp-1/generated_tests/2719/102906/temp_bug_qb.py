def original_func(*args):
	global_list = []
	
	ans = 0
	rawInp = args[0].split(' ')
	(a, b) = (rawInp[0], rawInp[1])
	while (a > b):
	    a *= 3
	    b *= 2
	    ans += 1
	global_list.append(ans)
	return global_list