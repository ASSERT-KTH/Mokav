def patched_func(*args):
	global_list = []
	
	A = args[0]
	c = 0
	count = 0
	for i in A:
	    if ((i == '4') or (i == '7')):
	        count = (count + 1)
	b = str(count)
	for i in b:
	    if ((i != '4') and (i != '7')):
	        c = 1
	        break
	if (c == 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list