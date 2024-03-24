def func(*args):
	ret_values = []
	
	'input\n2\n3\n4\n5\n24\n'
	(k, l, m, n, d) = [int(args[0]) for _ in range(5)]
	unharmed = 0
	if (min([k, l, m, m]) == 1):
	    ret_values.append(d)
	else:
	    for x in range(1, (d + 1)):
	        if all((((x % i) != 0) for i in [k, l, m, n])):
	            unharmed += 1
	    ret_values.append((d - unharmed))

	return ret_values
