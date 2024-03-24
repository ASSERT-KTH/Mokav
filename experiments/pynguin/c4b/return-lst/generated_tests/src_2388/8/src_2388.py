def func(*args):
	ret_values = []
	
	consonents = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
	s = args[0]
	t = ''
	for x in s:
	    if (x in consonents):
	        continue
	    elif (ord(x) < 97):
	        t = ((t + '.') + chr((ord(x) + 32)))
	    else:
	        t = ((t + '.') + x)
	ret_values.append(t)

	return ret_values
