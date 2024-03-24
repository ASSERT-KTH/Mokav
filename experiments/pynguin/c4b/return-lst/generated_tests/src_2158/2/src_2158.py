def func(*args):
	ret_values = []
	
	n = args[0]
	if (n[3:] >= (n[1] + n[0])):
	    n = str(((int(n[:2]) + 1) % 24))
	    if (len(n) == 1):
	        n = ('0' + n)
	else:
	    n = n[:2]
	n = (((n + ':') + n[1]) + n[0])
	if (n[1] > '5'):
	    if (n[0] == '1'):
	        n = '20:02'
	    else:
	        n = '10:01'
	ret_values.append(n)

	return ret_values
