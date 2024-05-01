def patched_func(*args):
	global_list = []
	
	up = True
	s = args[0]
	if (len(s) == 1):
	    if s.islower():
	        s = s.upper()
	    else:
	        s = s.lower()
	else:
	    for i in range(1, len(s)):
	        if (not s[i].isupper()):
	            up = False
	            break
	    if (up and s[0].isupper()):
	        s = s.lower()
	    elif (up and s[0].islower()):
	        s = (s[0].upper() + s[1:].lower())
	global_list.append(s)
	return global_list