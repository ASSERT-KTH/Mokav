def func(*args):
	ret_values = []
	
	(a, b, c) = [int(i) for i in args[0].split()]
	if (c == 0):
	    if (a == b):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif (c > 0):
	    if (((b % c) == (a % c)) and (b >= a)):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')
	elif ((a >= b) and ((b % (- c)) == (a % (- c)))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
