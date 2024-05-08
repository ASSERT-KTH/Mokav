def patched_func(*args):
	global_list = []
	
	a = args[0]
	if ((a[0].islower() and a[1:].isupper()) or (a.islower() and (len(a) == 1))):
	    global_list.append((a[0].upper() + a[1:].lower()))
	elif a.isupper():
	    global_list.append(a.lower())
	else:
	    global_list.append(a)
	return global_list