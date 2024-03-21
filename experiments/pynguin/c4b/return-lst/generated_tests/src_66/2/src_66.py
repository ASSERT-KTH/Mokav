def func(*args):
	ret_values = []
	
	l = [int(x) for x in args[0].split()]
	ans = 0
	d = []
	for e in l:
	    if (e in d):
	        ans += 1
	    else:
	        d.append(e)
	ret_values.append(ans)

	return ret_values
