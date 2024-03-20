def func(*args):
	
	table = ['1/1', '5/6', '2/3', '1/2', '1/3', '1/6']
	(a, b) = map(int, args[0].split())
	return(table[(max(a, b) - 1)])
