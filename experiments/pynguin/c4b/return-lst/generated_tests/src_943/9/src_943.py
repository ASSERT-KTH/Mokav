def func(*args):
	ret_values = []
	
	from sys import exit
	(a, b, c) = [int(i) for i in args[0].split()]
	for i in range((c + 1)):
	    if (((a * i) <= c) and (((c - (a * i)) % b) == 0)):
	        ret_values.append('Yes')
	        exit(0)
	ret_values.append('No')

	return ret_values
