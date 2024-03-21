def func(*args):
	ret_values = []
	
	n = args[0]
	k = len(n)
	m = 0
	j = 0
	for i in range((k - 1)):
	    if (n[i] == n[(i + 1)]):
	        j = (j + 1)
	        if (j == 6):
	            ret_values.append('YES')
	            break
	    else:
	        j = 0
	if (j < 6):
	    ret_values.append('NO')

	return ret_values
