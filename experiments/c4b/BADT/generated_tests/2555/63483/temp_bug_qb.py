def original_func(*args):
	global_list = []
	
	d = args[0]
	p = True
	for i in range((len(d) - 1)):
	    m = i
	    j = 0
	    while (d[m] == d[(m + 1)]):
	        m += 1
	        j += 1
	    if (j >= 7):
	        global_list.append('YES')
	        p = False
	        break
	if p:
	    global_list.append('NO')
	return global_list