def func(*args):
	ret_values = []
	
	s = args[0]
	for i in range(1, len(s)):
	    if (ord(s[i]) > 90):
	        ret_values.append(s)
	        exit()
	if (ord(s[0]) > 90):
	    ret_values.append((s[0].upper() + s[1:].lower()))
	else:
	    ret_values.append(s.lower())

	return ret_values
