def original_func(*args):
	global_list = []
	
	s = args[0]
	a = ['H', 'Q', '9', '+']
	i = 0
	while (i < len(s)):
	    if (s[i] in a):
	        message = 'YES'
	        break
	    else:
	        message = 'NO'
	    i += 1
	global_list.append(message)
	return global_list