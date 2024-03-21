def func(*args):
	ret_values = []
	
	from sys import exit
	(a, b) = [int(x) for x in args[0].split()]
	if ((a == 0) and (b == 0)):
	    ret_values.append('NO')
	    exit()
	if (abs((a - b)) > 1):
	    ret_values.append('NO')
	    exit()
	else:
	    ret_values.append('YES')
	    exit()

	return ret_values
