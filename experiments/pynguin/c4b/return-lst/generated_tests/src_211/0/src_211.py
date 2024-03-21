def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	s = int((a ** 0.5))
	if ((s * (s + 1)) > b):
	    ret_values.append('Valera')
	else:
	    ret_values.append('Vladik')

	return ret_values
