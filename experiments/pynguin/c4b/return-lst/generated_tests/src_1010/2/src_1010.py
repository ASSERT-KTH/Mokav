def func(*args):
	ret_values = []
	
	s = list(args[0])
	L = ['Q', 'H', '9']
	q = 0
	for i in s:
	    if (i in L):
	        ret_values.append('YES')
	        q = 1
	        break
	if (q == 0):
	    ret_values.append('NO')

	return ret_values
