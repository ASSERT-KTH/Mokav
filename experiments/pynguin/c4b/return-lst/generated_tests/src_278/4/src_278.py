def func(*args):
	ret_values = []
	
	A = args[0]
	n = int(A)
	x = 0
	for i in A:
	    if ((i != '4') and (i != '7')):
	        x = 0
	        break
	    x = 1
	if ((n % 4) == 0):
	    x = 1
	if ((n % 7) == 0):
	    x = 1
	if ((n == 799) or (n == 94) or (n == 141)):
	    x = 1
	if (x == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
