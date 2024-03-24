def func(*args):
	ret_values = []
	
	from sys import stdin
	txt = stdin.readline()
	p = ((((txt[0] + txt[2]) + txt[4]) + txt[3]) + txt[1])
	m = n = int(p)
	n = ((n * n) % 100000)
	n = ((n * n) % 100000)
	n = ((n * m) % 100000)
	ret_values.append('{0:0=5d}'.format(n))

	return ret_values
