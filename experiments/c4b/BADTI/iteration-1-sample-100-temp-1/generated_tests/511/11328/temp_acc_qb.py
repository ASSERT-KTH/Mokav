def patched_func(*args):
	global_list = []
	
	(a, b, d) = [int(i) for i in args[0].split()]
	try:
	    if ((((b - a) % d) == 0) and (((b - a) / d) >= 0)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	except:
	    if (a == b):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list