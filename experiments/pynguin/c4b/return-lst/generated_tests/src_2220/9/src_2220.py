def func(*args):
	ret_values = []
	
	s = args[0]
	a = 'hello'
	k = 0
	for i in s:
	    if (i == a[k]):
	        k += 1
	    if (k == 5):
	        ret_values.append('YES')
	        exit()
	ret_values.append('NO')

	return ret_values
