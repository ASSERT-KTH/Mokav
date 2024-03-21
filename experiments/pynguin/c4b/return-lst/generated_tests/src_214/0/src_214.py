def func(*args):
	ret_values = []
	
	l = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
	n = (int(args[0]) - 1)
	p = 0
	w = (- 1)
	while True:
	    w += 1
	    p += (5 * (2 ** w))
	    if (p > n):
	        p -= (5 * (2 ** w))
	        k = (n - p)
	        ret_values.append(l[(k // (2 ** w))])
	        break

	return ret_values
