def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (a, b) = str(args[0]).split()
	    (a, b) = (int(a), int(b))
	    value = 0
	    if ((abs((a - b)) % 3) == 0):
	        value = ((a + b) - 3)
	    else:
	        value = ((a + b) - 2)
	    if ((a == 1) and (b == 1)):
	        value = 0
	    ret_values.append(value)

	return ret_values
