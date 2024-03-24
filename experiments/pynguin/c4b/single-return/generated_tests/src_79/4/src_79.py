def func(*args):
	
	n = int(args[0])
	a = [int(i) for i in args[1].split()]
	b = (3 * [0])
	d = ['chest', 'biceps', 'back']
	for i in range(n):
	    b[(i % 3)] += a[i]
	z = b.index(max(b))
	return(d[z])
