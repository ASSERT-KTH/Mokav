def original_func(*args):
	global_list = []
	
	z = args[0]
	t = 1
	summ = 0
	k = 0
	for e in str(z):
	    global_list.append(e)
	    if ((e == '4') or (e == '7')):
	        k += 1
	for e in str(k):
	    if ((e != '4') and (e != '7')):
	        global_list.append('NO')
	        t = 0
	        break
	if t:
	    global_list.append('YES')
	return global_list