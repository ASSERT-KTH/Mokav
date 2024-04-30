def original_func(*args):
	global_list = []
	
	x = args[0]
	x = str(x)
	ans = 0
	o = 0
	z = 0
	isdanger = False
	for i in range(x.__len__()):
	    if (x[(i - 1)] == '0'):
	        z += 1
	        o = 0
	        if (z >= 7):
	            isdanger = True
	    else:
	        z = 0
	        o += 1
	        if (o >= 7):
	            isdanger = True
	if isdanger:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list