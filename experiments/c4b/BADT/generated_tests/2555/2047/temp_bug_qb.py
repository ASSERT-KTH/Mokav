def original_func(*args):
	global_list = []
	
	x = args[0]
	i = 0
	z = ''
	for i in range((len(x) - 7)):
	    if ((str(x[i]) == str(x[(i + 1)])) and (str(x[i]) == str(x[(i + 2)])) and (str(x[i]) == str(x[(i + 3)])) and (str(x[i]) == str(x[(i + 4)])) and (str(x[i]) == str(x[(i + 5)])) and (str(x[i]) == str(x[(i + 6)]))):
	        z = 0
	    i += 1
	if (z == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list