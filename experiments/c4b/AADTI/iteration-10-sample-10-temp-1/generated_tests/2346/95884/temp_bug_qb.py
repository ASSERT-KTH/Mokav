def original_func(*args):
	global_list = []
	
	x = args[0].split()
	x.sort()
	for i in range(len(x)):
	    x[i] = int(x[i])
	x.sort()
	n = 100
	for j in range(2):
	    if ((x[j] + x[(j + 1)]) > x[(j + 2)]):
	        n = 300
	    elif ((x[j] + x[(j + 1)]) == x[(j + 2)]):
	        n = max(n, 200)
	    else:
	        n = max(n, 100)
	if (n == 300):
	    global_list.append('TRIANGLE')
	elif (n == 200):
	    global_list.append('SIGMENT')
	else:
	    global_list.append('IMPOSSIBLE')
	return global_list