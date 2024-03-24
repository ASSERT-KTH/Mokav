def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	if ((c < 0) and (a < b)):
	    ret_values.append('NO')
	    exit(0)
	if ((c > 0) and (a > b)):
	    ret_values.append('NO')
	    exit(0)
	if ((c == 0) and (a == b)):
	    ret_values.append('YES')
	    exit(0)
	if ((c == 0) and (a != b)):
	    ret_values.append('NO')
	    exit(0)
	if ((abs((a - b)) % abs(c)) != 0):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
