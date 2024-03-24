def func(*args):
	ret_values = []
	
	d = []
	anz = 0
	(a, b, c) = [int(x) for x in args[0].split()]
	d.append(a)
	d.append(b)
	d.append(c)
	d.sort()
	anz = (d[2] - d[0])
	ret_values.append(anz, end='\n')

	return ret_values
