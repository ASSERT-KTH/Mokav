def func(*args):
	ret_values = []
	
	(x, t, a, b, dA, dB) = map(int, args[0].split())
	if ((x == 0) or (a == x) or (b == x)):
	    ret_values.append('YES')
	    exit()
	tempA = a
	tempB = b
	for i in range(t):
	    tempA = (a - (i * dA))
	    tempB = b
	    for j in range(t):
	        tempB = (b - (j * dB))
	        if (((tempA + tempB) == x) or (tempA == x) or (tempB == x)):
	            ret_values.append('YES')
	            exit()
	ret_values.append('NO')

	return ret_values
