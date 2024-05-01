def patched_func(*args):
	global_list = []
	
	l = [int(x) for x in args[0].split()]
	ans = 0
	d = []
	for e in l:
	    if (e in d):
	        ans += 1
	    else:
	        d.append(e)
	global_list.append(ans)
	return global_list