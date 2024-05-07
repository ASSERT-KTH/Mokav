def patched_func(*args):
	global_list = []
	
	(a, b, c, d) = sorted((int(x) for x in args[0].split()))
	if (((a + b) > c) or ((b + c) > d)):
	    global_list.append('TRIANGLE')
	elif (((a + b) == c) or ((a + b) == d) or ((b + c) == d)):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list