def func(*args):
	ret_values = []
	
	s = args[0]
	i = 0
	j = 0
	for char in s:
	    if ((ord(char) >= 97) and (ord(char) <= 122)):
	        i += 1
	    else:
	        j += 1
	if (i >= j):
	    ret_values.append(s.lower())
	else:
	    ret_values.append(s.upper())

	return ret_values
