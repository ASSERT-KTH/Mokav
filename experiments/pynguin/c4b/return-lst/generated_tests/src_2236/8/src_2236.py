def func(*args):
	ret_values = []
	
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
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
