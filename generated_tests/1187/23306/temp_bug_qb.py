def original_func(*args):
	global_list = []
	
	T = args[0]
	if ((len(T) == 1) and T.islower):
	    T = T.upper()
	elif (T[0].islower() and T[1:len(T)].isupper()):
	    T = T.capitalize()
	    T[1:len(T)].lower()
	elif T.isupper():
	    T = T.lower()
	global_list.append(T)
	return global_list