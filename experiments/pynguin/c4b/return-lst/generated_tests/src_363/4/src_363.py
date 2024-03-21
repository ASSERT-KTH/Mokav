def func(*args):
	ret_values = []
	
	a = args[0]
	l = 0
	u = 0
	for i in a:
	    if i.islower():
	        l += 1
	    else:
	        u += 1
	if (l >= u):
	    ret_values.append(a.lower())
	else:
	    ret_values.append(a.upper())

	return ret_values
