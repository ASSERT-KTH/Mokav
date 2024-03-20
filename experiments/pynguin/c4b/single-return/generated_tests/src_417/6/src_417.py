def func(*args):
	
	position = [int(i) for i in args[0].split()]
	position.sort()
	return(((position[2] - position[1]) + (position[1] - position[0])))
