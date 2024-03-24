def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (x, y) = args[0].split()
	    n = int(args[1])
	    dirs = {'^': 1, '>': 2, 'v': 3, '<': 4}
	    if ((n % 2) == 0):
	        ret_values.append('undefined')
	    elif (((dirs[y] - dirs[x]) % 4) == (n % 4)):
	        ret_values.append('cw')
	    else:
	        ret_values.append('ccw')

	return ret_values
