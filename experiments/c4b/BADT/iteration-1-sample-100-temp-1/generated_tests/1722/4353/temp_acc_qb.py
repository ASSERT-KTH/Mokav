def patched_func(*args):
	global_list = []
	
	f = (lambda x, y: bool(set(str(x)).__rand__(set(str(y)))))
	x = int(args[0])
	k = 0
	i = 1
	while ((i * i) <= x):
	    if ((x % i) == 0):
	        k += f(x, i)
	        t = (x // i)
	        if (t != i):
	            k += f(x, t)
	    i += 1
	global_list.append(k)
	return global_list