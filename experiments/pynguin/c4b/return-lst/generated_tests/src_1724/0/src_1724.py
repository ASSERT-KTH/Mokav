def func(*args):
	ret_values = []
	
	k = args[0].split()
	r = int(k[0])
	p = int(k[1])
	m = int(k[2])
	ret_values.append(((((m + 1) // 2) + (p - 1)) // p), end=' ')
	ret_values.append((((m + 1) // 2) - ((((((m + 1) // 2) + (p - 1)) // p) - 1) * p)), end=' ')
	if ((m % 2) == 0):
	    ret_values.append('R')
	else:
	    ret_values.append('L')

	return ret_values
