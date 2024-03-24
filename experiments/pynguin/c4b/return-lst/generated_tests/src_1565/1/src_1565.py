def func(*args):
	ret_values = []
	
	a = int(args[0])
	b = bin(a)
	i = 2
	while (i < len(b)):
	    if (b[i] == '1'):
	        ret_values.append((len(b) - i), end=' ')
	    i += 1

	return ret_values
