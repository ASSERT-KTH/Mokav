def func(*args):
	ret_values = []
	
	(A, B, n) = map(int, args[0].split())
	if ((A == 0) and (B == 0)):
	    ret_values.append(5)
	elif (A == 0):
	    ret_values.append('No solution')
	elif (((B / A) % 1) != 0):
	    ret_values.append('No solution')
	else:
	    v = (B // A)
	    if (v < 0):
	        x = (- 1)
	    else:
	        x = 1
	    v = pow(abs(v), (1 / n))
	    vv = round(v)
	    if (abs((vv - v)) > (10 ** (- 6))):
	        ret_values.append('No solution')
	    else:
	        ret_values.append((x * int(vv)))

	return ret_values
