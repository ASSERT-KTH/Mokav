def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    refer = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	    (m, d) = map(int, args[0].split())
	    n = ((refer[m] + d) - 8)
	    for i in range(1, 7):
	        if (n <= 0):
	            ret_values.append(i)
	            break
	        n -= 7

	return ret_values
