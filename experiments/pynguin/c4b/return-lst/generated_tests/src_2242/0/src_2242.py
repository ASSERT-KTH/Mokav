def func(*args):
	ret_values = []
	
	p = str(args[0])
	a = False
	for i in range(len(p)):
	    if ((p[i] == 'H') or (p[i] == 'Q') or (p[i] == '9')):
	        a = True
	        break
	if (a == True):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
