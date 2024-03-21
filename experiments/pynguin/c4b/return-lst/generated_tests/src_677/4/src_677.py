def func(*args):
	ret_values = []
	
	n = int(args[0])
	from sys import exit
	if (n < 3):
	    ret_values.append(n)
	    exit(0)
	if ((n % 2) != 0):
	    ret_values.append(((n * (n - 1)) * (n - 2)))
	    exit(0)
	if ((n % 3) == 0):
	    ret_values.append((((n - 3) * (n - 1)) * (n - 2)))
	    exit(0)
	ret_values.append((((n - 1) * n) * (n - 3)))

	return ret_values
