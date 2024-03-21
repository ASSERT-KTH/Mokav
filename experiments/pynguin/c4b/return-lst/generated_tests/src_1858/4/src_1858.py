def func(*args):
	ret_values = []
	
	line = args[0]
	res = []
	for e in line:
	    if (len(res) > 0):
	        if (res[(- 1)] == '/'):
	            if (e == '/'):
	                continue
	            else:
	                res.append(e)
	        else:
	            res.append(e)
	    else:
	        res.append(e)
	if (len(res) == 1):
	    ret_values.append(''.join(res))
	else:
	    i = (len(res) - 1)
	    while ((res[i] == '/') and (i > 0)):
	        i -= 1
	    ret_values.append(''.join(res[:(i + 1)]))

	return ret_values
