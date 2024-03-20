def func(*args):
	
	from math import ceil
	q = args[0].split(' ')
	a = int(q[2])
	n = int(q[0])
	m = int(q[1])
	answer = (ceil((m / a)) * ceil((n / a)))
	return(answer)
