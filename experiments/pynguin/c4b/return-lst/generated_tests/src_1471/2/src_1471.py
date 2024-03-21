def func(*args):
	ret_values = []
	
	n = args[0]
	a = (n.count('4') + n.count('7'))
	s = str(a)
	for i in s:
	    if ((i != '4') and (i != '7')):
	        ret_values.append('NO')
	        raise SystemExit
	ret_values.append('YES')

	return ret_values
