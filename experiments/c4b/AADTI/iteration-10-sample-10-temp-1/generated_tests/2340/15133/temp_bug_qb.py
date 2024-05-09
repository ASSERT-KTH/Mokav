def original_func(*args):
	global_list = []
	
	s = args[0]
	i = 0
	j = 0
	for char in s:
	    if ((ord(char) >= 97) and (ord(char) <= 122)):
	        i += 1
	    else:
	        j += 1
	if (i == j):
	    global_list.append(s.lower())
	else:
	    global_list.append(s.upper())
	return global_list