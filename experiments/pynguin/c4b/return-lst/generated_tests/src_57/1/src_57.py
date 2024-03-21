def func(*args):
	ret_values = []
	
	a = int(args[0])
	x = ''
	while a:
	    if (a % 2):
	        x = ('that I hate ' + x)
	    else:
	        x = ('that I love ' + x)
	    a -= 1
	ret_values.append((x[5:] + 'it'))

	return ret_values
