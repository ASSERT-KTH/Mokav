def func(*args):
	
	coords = list(map(int, args[0].split()))
	coords.sort()
	return((coords[2] - coords[0]))
