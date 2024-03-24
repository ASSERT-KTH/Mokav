def func(*args):
	ret_values = []
	
	t = args[0]
	res = 0
	for i in t:
	    if ((i == '4') or (i == '7')):
	        res += 1
	if ((res == 4) or (res == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
