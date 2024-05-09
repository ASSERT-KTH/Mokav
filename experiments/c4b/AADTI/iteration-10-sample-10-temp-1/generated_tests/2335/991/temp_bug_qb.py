def original_func(*args):
	global_list = []
	
	x = args[0]
	i = 0
	p = 0
	l = ''
	for h in 'hello':
	    while ((h != l) and (i < len(x))):
	        l = x[i]
	        i += 1
	    if ((i != len(x)) or ((h == 'o') and (l == 'o'))):
	        p += 1
	if (p == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list