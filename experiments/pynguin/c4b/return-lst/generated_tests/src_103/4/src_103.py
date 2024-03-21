def func(*args):
	ret_values = []
	
	s = args[0]
	n = len(s)
	l = 0
	for i in range(n):
	    if (s[i] != s[((n - 1) - i)]):
	        l += 1
	if ((l == 2) or ((l == 0) and ((n % 2) == 1))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
