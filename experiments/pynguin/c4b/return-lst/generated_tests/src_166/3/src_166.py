def func(*args):
	ret_values = []
	
	'input\n105\n106\n'
	(a, b) = (args[0], args[1])
	s = str((int(a) + int(b))).replace('0', '')
	if ((int(a.replace('0', '')) + int(b.replace('0', ''))) == int(s)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
