def func(*args):
	ret_values = []
	
	integer = int(args[0])
	types = (('byte', 7), ('short', 15), ('int', 31), ('long', 63), ('BigInteger', 100000))
	ret_values.append([type_ for (type_, val) in types if ((2 ** val) > integer)][0])

	return ret_values
