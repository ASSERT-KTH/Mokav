def original_func(*args):
	global_list = []
	
	p = args[0]
	a = p[0]
	cnt = 1
	for i in range(1, len(p)):
	    if (p[i] == a):
	        cnt = (cnt + 1)
	    else:
	        a = p[i]
	        cnt = 1
	    if (cnt == 7):
	        global_list.append('YES')
	        break
	if (i == (len(p) - 1)):
	    global_list.append('NO')
	return global_list