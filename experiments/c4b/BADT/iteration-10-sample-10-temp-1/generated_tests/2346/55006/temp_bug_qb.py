def original_func(*args):
	global_list = []
	
	(a, b, c, d) = map(int, args[0].split())
	l = [a, b, c, d]
	k = max(l)
	for x in l:
	    if (x == k):
	        l.remove(x)
	        break
	if (((l[0] + l[1]) > k) or ((l[0] + l[2]) > k) or ((l[1] + l[2]) > k)):
	    global_list.append('TRIANGLE')
	elif (((l[0] + l[1]) == k) or ((l[0] + l[2]) == k) or ((l[1] + l[2]) == k)):
	    global_list.append('SEGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list