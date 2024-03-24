def func(*args):
	ret_values = []
	
	s = args[0]
	(a, b) = (0, 0)
	for c in s:
	    if c.isupper():
	        a = (a + 1)
	    else:
	        b = (b + 1)
	if (a > b):
	    ret_values.append(s.upper())
	elif (a < b):
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s.lower())

	return ret_values
