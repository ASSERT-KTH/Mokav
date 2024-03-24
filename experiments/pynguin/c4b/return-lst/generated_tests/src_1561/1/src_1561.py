def func(*args):
	ret_values = []
	
	from sys import stdin
	i = [x.rstrip() for x in stdin.readlines()]
	it = int(i[0].split()[1])
	q = [c for c in i[1]]
	l = len(q)
	steps = (l * it)
	x = 0
	while (x < steps):
	    if ((q[(x % l)] == 'B') and (q[((x + 1) % l)] == 'G')):
	        (q[(x % l)], q[((x + 1) % l)]) = ('G', 'B')
	        x += 1
	    x += 1
	    if (not ((x + 1) % l)):
	        x += 1
	ret_values.append(''.join(q))

	return ret_values
