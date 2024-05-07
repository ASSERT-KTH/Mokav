def patched_func(*args):
	global_list = []
	
	x = args[0]
	
	def f(v):
	    if v.isupper():
	        return v.lower()
	    return v.upper()
	if ((len(x) < 2) or x[1:].isupper()):
	    x = (f(x[0]) + x[1:].lower())
	global_list.append(x)
	return global_list