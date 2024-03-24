def func(*args):
	
	(d1, d2, d3) = map((lambda x: int(x)), args[0].split(' '))
	path = 0
	path += min(d1, d2)
	path += min((d1 + d2), d3)
	path += min(max(d1, d2), (min(d1, d2) + d3))
	return(path)
