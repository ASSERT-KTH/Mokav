def func(*args):
	ret_values = []
	
	from math import ceil
	q = args[0].split(' ')
	a = int(q[2])
	n = int(q[0])
	m = int(q[1])
	answer = (ceil((m / a)) * ceil((n / a)))
	ret_values.append(answer)

	return ret_values
