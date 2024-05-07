def patched_func(*args):
	global_list = []
	
	s = args[0]
	if s.isupper():
	    s = s.lower()
	elif (len(s) == 1):
	    s = s.upper()
	elif (s[0].islower() and s[1:].isupper()):
	    s = (s[0].upper() + s[1:].lower())
	global_list.append(s)
	return global_list