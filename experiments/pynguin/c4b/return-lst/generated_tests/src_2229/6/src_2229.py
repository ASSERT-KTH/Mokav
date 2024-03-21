def func(*args):
	ret_values = []
	
	A = args[0]
	k = 0
	while ((A[k] != 'H') and (A[k] != 'Q') and (A[k] != '9') and (k < (len(A) - 1))):
	    k += 1
	if (k < (len(A) - 1)):
	    ret_values.append('YES')
	elif ((k == (len(A) - 1)) and ((A[k] == 'Q') or (A[k] == 'H') or (A[k] == '9'))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
