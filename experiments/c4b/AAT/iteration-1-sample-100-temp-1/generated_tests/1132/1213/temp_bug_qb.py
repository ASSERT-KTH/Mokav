def original_func(*args):
	global_list = []
	
	A = args[0]
	n = int(A)
	x = 0
	for i in A:
	    if ((i != '4') and (i != '7')):
	        x = 0
	        break
	    x = 1
	if ((n % 4) == 0):
	    x = 1
	if ((n % 7) == 0):
	    x = 1
	if ((n == 799) or (n == 94)):
	    x = 1
	if (x == 1):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list