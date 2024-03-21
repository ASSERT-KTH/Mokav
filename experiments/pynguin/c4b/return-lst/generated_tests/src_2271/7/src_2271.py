def func(*args):
	ret_values = []
	
	a = args[0]
	arr = []
	if (len(a) >= 7):
	    for i in range((len(a) - 6)):
	        b = a[i:(i + 7)]
	        if (len(set(b)) == 1):
	            arr.append('YES')
	        else:
	            arr.append('NO')
	if ('YES' in arr):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
