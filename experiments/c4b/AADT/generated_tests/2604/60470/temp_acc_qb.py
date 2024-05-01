def patched_func(*args):
	global_list = []
	
	x = args[0]
	y = []
	y1 = []
	for i in range(len(x)):
	    y.append(int(x[i]))
	    y1.append(int(x[i]))
	a = sum(y)
	i = (len(x) - 2)
	while (i >= 0):
	    if (y[i] != 0):
	        y[i] -= 1
	        for j in range((i + 1), len(x)):
	            y[j] = 9
	    b = sum(y)
	    if (b > a):
	        a = b
	        for j in range(len(y)):
	            y1[j] = y[j]
	    i -= 1
	k = ''
	for i in range(1, len(y1)):
	    k += str(y1[i])
	if (y1[0] != 0):
	    k = (str(y1[0]) + k)
	global_list.append(k)
	return global_list