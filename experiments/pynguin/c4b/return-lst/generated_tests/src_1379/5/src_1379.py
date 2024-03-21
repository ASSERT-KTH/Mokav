def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split()))
	if (((a[0] * a[2]) * a[4]) < ((a[1] * a[3]) * a[5])):
	    ret_values.append('Ron')
	elif ((0 == ((a[0] * a[2]) * a[4])) ^ (0 == ((a[1] * a[3]) * a[5]))):
	    ret_values.append('Hermione')
	elif (0 == ((a[0] * a[2]) * a[4]) == ((a[1] * a[3]) * a[5])):
	    if (((a[2] == 0) and (a[3] != 0)) or ((a[0] == 0) and (a[1] > 0) and (a[3] > 0))):
	        ret_values.append('Ron')
	    else:
	        ret_values.append('Hermione')
	else:
	    ret_values.append('Hermione')

	return ret_values
