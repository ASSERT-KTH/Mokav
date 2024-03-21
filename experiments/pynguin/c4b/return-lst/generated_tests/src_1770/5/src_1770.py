def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = (2 ** n)
	if (n >= 13):
	    a -= ((2 ** (n - 13)) * 100)
	ret_values.append(a)

	return ret_values
