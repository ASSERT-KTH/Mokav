def func(*args):
	ret_values = []
	
	x = args[0]
	a = ['h', 'e', 'l', 'l', 'o']
	for i in x:
	    if (len(a) == 0):
	        break
	    if (i == a[0]):
	        del a[0]
	if (len(a) == 0):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
