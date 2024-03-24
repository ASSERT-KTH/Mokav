def func(*args):
	
	n = args[0]
	k = n
	if n.isupper():
	    k = n.lower()
	elif n[1:].isupper():
	    k = n[0].upper()
	    k += n[1:].lower()
	if ((len(n) == 1) and n.islower()):
	    k = n.upper()
	if ((len(n) == 1) and n.isupper()):
	    k = n.lower()
	return(k)
