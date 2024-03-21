def func(*args):
	ret_values = []
	
	x = args[0]
	
	def f(v):
	    if v.isupper():
	        return v.lower()
	    return v.upper()
	if ((len(x) < 2) or x[1:].isupper()):
	    x = (f(x[0]) + x[1:].lower())
	ret_values.append(x)

	return ret_values
