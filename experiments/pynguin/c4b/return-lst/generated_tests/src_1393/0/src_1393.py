def func(*args):
	ret_values = []
	
	(n, k) = [int(x) for x in args[0].split(' ')]
	symbols = 'abcdefghijklmnopqrstuvwxyz'
	newPsw = ''
	q = 0
	for i in range(n):
	    if (q == k):
	        q = 0
	    newPsw += symbols[q]
	    q += 1
	ret_values.append(newPsw)

	return ret_values
