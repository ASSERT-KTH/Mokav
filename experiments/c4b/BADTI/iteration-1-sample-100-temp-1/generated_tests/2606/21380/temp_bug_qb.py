def original_func(*args):
	global_list = []
	
	(n, k) = map(int, args[0].split(' '))
	symbols = 'abcdefghijklmnopqrstuvwxyz'
	newPsw = ''
	q = 0
	fx = (lambda q: (q + 1))
	for i in range(n):
	    newPsw += symbols[q]
	    q = (0 if (q == k) else fx(q))
	global_list.append(newPsw)
	return global_list