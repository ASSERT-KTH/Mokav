def func(*args):
	
	(h, m) = map(int, args[0].split(':'))
	m += int(args[1])
	h = ((h + (m // 60)) % 24)
	m = (m % 60)
	f = (lambda x: (('0' * (not (x // 10))) + str(x)))
	return(((f(h) + ':') + f(m)))
