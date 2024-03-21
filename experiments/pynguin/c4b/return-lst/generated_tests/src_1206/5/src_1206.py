def func(*args):
	ret_values = []
	
	import sys
	(a, b, c, d, e, f) = [float(x) for x in sys.stdin.readline().split()]
	if ((c == 0) and (d != 0)):
	    ret_values.append('Ron')
	elif (d == 0):
	    ret_values.append('Hermione')
	elif ((a == 0) and (b != 0)):
	    ret_values.append('Ron')
	elif (b == 0):
	    ret_values.append('Hermione')
	elif ((e == 0) and (f != 0)):
	    ret_values.append('Ron')
	elif (f == 0):
	    ret_values.append('Hermione')
	else:
	    v = (((b / a) * (d / c)) * (f / e))
	    if (v <= 1):
	        ret_values.append('Hermione')
	    else:
	        ret_values.append('Ron')

	return ret_values
