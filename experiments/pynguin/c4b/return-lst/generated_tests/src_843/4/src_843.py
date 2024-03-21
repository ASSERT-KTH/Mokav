def func(*args):
	ret_values = []
	
	numbers = [int(x) for x in args[0].split(' ')]
	a = numbers[0]
	b = numbers[1]
	for i in range(1, 100000):
	    if (((((a * i) - b) % 10) == 0) or (((a * i) % 10) == 0)):
	        ret_values.append(i)
	        break

	return ret_values
