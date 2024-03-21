def func(*args):
	ret_values = []
	
	n = int(args[0])
	get = []
	x = 1
	out = ''
	for i in range(1, n):
	    x = (x + i)
	    if (x > n):
	        x = (x % n)
	    if (i == (n - 1)):
	        out += str(x)
	    else:
	        out += (str(x) + ' ')
	ret_values.append(out)

	return ret_values
