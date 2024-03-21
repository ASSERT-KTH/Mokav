def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split(' '))
	if (c == 0):
	    if (b == a):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif ((((b - a) % c) == 0) and (((c > 0) and (a <= b)) or ((c < 0) and (a >= b)))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
