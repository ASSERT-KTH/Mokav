def func(*args):
	
	string = args[0]
	numbers = string.split(' ')
	n = int(numbers[0])
	a = int(numbers[1])
	b = int(numbers[2])
	x = (n - a)
	y = (((n - a) - b) - 1)
	if (y > 0):
	    x -= y
	return(x)
