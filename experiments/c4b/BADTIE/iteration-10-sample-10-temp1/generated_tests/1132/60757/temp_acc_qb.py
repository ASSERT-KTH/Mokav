def patched_func(*args):
	global_list = []
	
	s = args[0]
	lfl = 1
	alfl = 0
	n = ['4', '7']
	factors = []
	facl = []
	for i in range(1, ((int(s) // 2) + 1)):
	    if ((int(s) % i) == 0):
	        factors.append(i)
	for i in s:
	    if (i not in n):
	        lfl = 0
	for j in factors:
	    fl = 1
	    for i in str(j):
	        if (i not in n):
	            fl = 0
	    if (fl == 1):
	        facl.append(j)
	if (lfl or (len(facl) > 0)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list