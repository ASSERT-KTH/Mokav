def func(*args):
	
	(a, b, c) = map(int, args[0].split())
	sum = []
	sum.append(((a + b) + c))
	sum.append(((a * 2) + (b * 2)))
	sum.append(((a * 2) + (c * 2)))
	sum.append(((b * 2) + (c * 2)))
	return(min(sum))
