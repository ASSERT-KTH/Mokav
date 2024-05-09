def patched_func(*args):
	global_list = []
	
	import string
	s = args[0]
	if (s == s.upper()):
	    global_list.append(s.swapcase())
	elif ((s[0] == s[0].lower()) and (s[1:] == s[1:].upper())):
	    global_list.append(s.capitalize())
	else:
	    global_list.append(s)
	return global_list