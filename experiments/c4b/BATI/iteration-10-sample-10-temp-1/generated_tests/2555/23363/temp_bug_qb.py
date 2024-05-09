def original_func(*args):
	global_list = []
	
	team = args[0]
	d = 0
	d_max = 0
	current = team[0]
	for i in team:
	    if (i == current):
	        d += 1
	    else:
	        if (d > d_max):
	            d_max = d
	        current = i
	        d = 1
	if (d_max >= 7):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list