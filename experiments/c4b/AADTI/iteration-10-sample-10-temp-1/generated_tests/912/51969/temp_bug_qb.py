def original_func(*args):
	global_list = []
	
	(n, k) = list(map(int, args[0].strip().split(' ')))
	TIME = ((4 * 60) - k)
	for i in range(0, (n + 1)):
	    if (((5 * (i * (i + 1))) // 2) <= TIME):
	        1
	    else:
	        break
	ans = i
	global_list.append(ans)
	return global_list