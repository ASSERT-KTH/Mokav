def func(*args):
	ret_values = []
	
	s = args[0]
	num = 0
	for char in s:
	    if (char >= 'a'):
	        num += 1
	if (num >= (len(s) - num)):
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s.upper())

	return ret_values
