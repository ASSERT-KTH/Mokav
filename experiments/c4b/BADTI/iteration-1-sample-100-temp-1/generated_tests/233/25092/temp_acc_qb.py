def patched_func(*args):
	global_list = []
	
	n = int(args[0])
	a = int(args[1])
	b = int(args[2])
	c = int(args[3])
	a2 = (b - c)
	if ((a2 >= a) or (n < b)):
	    global_list.append((n // a))
	else:
	    ans = 0
	    ans += ((n - c) // (b - c))
	    n -= (ans * (b - c))
	    ans += (n // a)
	    global_list.append(ans)
	return global_list