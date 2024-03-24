def func(*args):
	ret_values = []
	
	R = (lambda : map(int, args[0].split()))
	(n, l) = R()
	if (((n != 0) or (l != 0)) and (((n - l) == 0) or ((n - l) == (- 1)) or ((n - l) == 1))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
