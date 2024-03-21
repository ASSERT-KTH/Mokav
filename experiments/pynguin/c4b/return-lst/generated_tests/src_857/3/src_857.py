def func(*args):
	ret_values = []
	
	st = args[0]
	length = len(st)
	count = 0
	if (length < 7):
	    ret_values.append('NO')
	else:
	    for i in range(length):
	        if (i == 0):
	            continue
	        if (st[i] == st[(i - 1)]):
	            count = (count + 1)
	            if (count >= 6):
	                ret_values.append('YES')
	                break
	        else:
	            if (count >= 6):
	                ret_values.append('YES')
	                break
	            count = 0
	    if (count < 6):
	        ret_values.append('NO')

	return ret_values
