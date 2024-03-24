def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    n = list(map(int, args[0].split()))
	    n.sort()
	    if ((n[0] + n[1]) > n[2]):
	        ret_values.append('TRIANGLE')
	    elif ((n[1] + n[2]) > n[3]):
	        ret_values.append('TRIANGLE')
	    elif ((n[0] + n[1]) == n[2]):
	        ret_values.append('SEGMENT')
	    elif ((n[1] + n[2]) == n[3]):
	        ret_values.append('SEGMENT')
	    else:
	        ret_values.append('IMPOSSIBLE')

	return ret_values
