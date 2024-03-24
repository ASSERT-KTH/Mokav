def func(*args):
	ret_values = []
	
	n = int(args[0])
	g = args[1]
	res = ([0] * 4)
	for i in g:
	    if (i in ['1', '2', '3']):
	        res[0] = 1
	    if (i in ['3', '6', '9']):
	        res[1] = 1
	    if (i in ['7', '0', '9']):
	        res[2] = 1
	    if (i in ['1', '4', '7']):
	        res[3] = 1
	if ((sum(res) == 4) or (res[0] and ('0' in g))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
