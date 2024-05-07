def patched_func(*args):
	global_list = []
	
	(a, b, c, d) = map(int, args[0].split())
	l = [a, b, c, d]
	l = sorted(l)
	if (((l[0] + l[1]) > l[3]) or ((l[0] + l[2]) > l[3]) or ((l[1] + l[2]) > l[3]) or ((l[0] + l[1]) > l[2])):
	    global_list.append('TRIANGLE')
	elif (((l[0] + l[1]) == l[3]) or ((l[0] + l[2]) == l[3]) or ((l[1] + l[2]) == l[3]) or ((l[0] + l[1]) == l[2])):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list