def func(*args):
	ret_values = []
	
	a = args[0]
	arr = ['H', 'Q', '9']
	narr = []
	for i in range(len(arr)):
	    if (arr[i] in a):
	        narr.append('YES')
	    else:
	        narr.append('NO')
	if ('YES' in narr):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
