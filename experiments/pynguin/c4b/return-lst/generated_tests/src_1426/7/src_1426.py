def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (a, b) = map(int, args[0].split(' '))
	    count = 0
	    while (a <= b):
	        count += 1
	        a = (a * 3)
	        b = (b * 2)
	    ret_values.append(count)

	return ret_values
