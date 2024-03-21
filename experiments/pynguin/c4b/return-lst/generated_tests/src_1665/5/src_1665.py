def func(*args):
	ret_values = []
	
	s = args[0]
	(k, n, z) = (0, (len(s) // 2), len(s))
	for i in range(n):
	    if (s[i] != s[((z - i) - 1)]):
	        k += 1
	if (k == 1):
	    ret_values.append('YES')
	elif ((k == 0) and ((z % 2) == 1)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
