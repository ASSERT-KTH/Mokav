def func(*args):
	ret_values = []
	
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
	    ret_values.append('TRIANGLE')
	elif (n == 200):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
