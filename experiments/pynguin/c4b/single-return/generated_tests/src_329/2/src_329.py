def func(*args):
	
	l = list(map(int, args[0].split(' ')))
	l.sort()
	a = l[0]
	b = l[1]
	c = l[2]
	one = ((a + b) + c)
	two = (2 * (a + b))
	return(min(one, two))
