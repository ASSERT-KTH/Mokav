def original_func(*args):
	global_list = []
	
	p = args[0]
	p.split()
	y = [int(i) for i in p]
	m = y[0]
	count = 1
	a = len(y)
	x = (- 1)
	for i in range(1, a):
	    if (count == 7):
	        x = 0
	        break
	    if (y[i] == m):
	        count = (count + 1)
	    else:
	        m = y[i]
	        count = 1
	if (x == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list