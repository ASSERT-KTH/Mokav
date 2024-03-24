def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	a.sort()
	if ((a[3] < (a[0] + a[1])) or (a[3] < (a[0] + a[2])) or (a[3] < (a[2] + a[1]))):
	    ret_values.append('TRIANGLE')
	elif (a[2] < (a[0] + a[1])):
	    ret_values.append('TRIANGLE')
	elif ((a[3] == (a[0] + a[1])) or (a[3] == (a[0] + a[2])) or (a[3] == (a[2] + a[1]))):
	    ret_values.append('SEGMENT')
	elif (a[2] == (a[0] + a[1])):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
