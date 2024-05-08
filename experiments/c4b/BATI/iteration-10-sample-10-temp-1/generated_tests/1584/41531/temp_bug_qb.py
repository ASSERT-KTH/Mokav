def original_func(*args):
	global_list = []
	
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
	    global_list.append(''.join(res))
	else:
	    i = (len(res) - 1)
	    while ((res[i] == '/') and (i > 0)):
	        i -= 1
	    global_list.append(''.join(res[:i]))
	return global_list