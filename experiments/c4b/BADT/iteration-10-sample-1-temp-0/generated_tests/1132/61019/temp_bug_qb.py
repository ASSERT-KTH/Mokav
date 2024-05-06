def original_func(*args):
	global_list = []
	
	x = int(args[0])
	a = 0
	j = 0
	if (((x % 4) == 0) or ((x % 7) == 0)):
	    global_list.append('YES')
	    j = 1
	x = str(x)
	x = list(x)
	if (j == 0):
	    for k in range(len(x)):
	        if ('7' in x):
	            y = x.index('7')
	            x[y] = '3'
	            a += 1
	        elif ('4' in x):
	            y = x.index('4')
	            x[y] = '3'
	            a += 1
	    if (a == len(x)):
	        global_list.append('YES')
	    else:
	        global_list.append('NO')
	return global_list