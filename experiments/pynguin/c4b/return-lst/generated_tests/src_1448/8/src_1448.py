def func(*args):
	ret_values = []
	
	s = args[0]
	n = len(s)
	com = 'hello'
	j = 0
	if (n < 5):
	    ret_values.append('NO')
	else:
	    for i in s:
	        if (com[j] == i):
	            j += 1
	        if (j > 4):
	            break
	    if (j > 4):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
