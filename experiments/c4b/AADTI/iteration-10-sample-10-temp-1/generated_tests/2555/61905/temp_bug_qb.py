def original_func(*args):
	global_list = []
	
	n = args[0]
	count = 0
	for i in range((len(n) - 1)):
	    if (n[i] == n[(i + 1)]):
	        count = (count + 1)
	if (count == 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list