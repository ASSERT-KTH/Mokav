def func(*args):
	ret_values = []
	
	T = args[0]
	if ((len(T) == 1) and T.islower()):
	    T = T.upper()
	elif ((len(T) == 1) and T.isupper()):
	    T = T.lower()
	elif (T[0].islower() and T[1:len(T)].isupper()):
	    T = T.capitalize()
	    T[1:len(T)].lower()
	elif T.isupper():
	    T = T.lower()
	ret_values.append(T)

	return ret_values
