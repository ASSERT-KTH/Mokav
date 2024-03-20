def func(*args):
	
	i = sorted(list(map(int, args[0].split())))
	return(min(((i[0] + i[1]) * 2), ((i[0] + i[2]) + i[1])))
