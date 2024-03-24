def func(*args):
	ret_values = []
	
	a = str(args[0])
	n = list(a)
	n.append(' ')
	k = 0
	z = False
	for k in range(len(n)):
	    if (n[k] == '1'):
	        t = 0
	        while (n[k] == '1'):
	            k += 1
	            t += 1
	        if (t >= 7):
	            z = True
	        k += 1
	    else:
	        t = 0
	        while (n[k] == '0'):
	            k += 1
	            t += 1
	        if (t >= 7):
	            z = True
	if (z == True):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
