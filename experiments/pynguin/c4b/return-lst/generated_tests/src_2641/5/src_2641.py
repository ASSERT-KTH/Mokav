def func(*args):
	ret_values = []
	
	a = args[0].split(' ')
	b = args[1].split(' ')
	if ((((int(a[2]) - int(a[0])) % int(b[0])) != 0) or (((int(a[3]) - int(a[1])) % int(b[1])) != 0)):
	    ret_values.append('NO')
	elif ((((int(a[2]) - int(a[0])) // int(b[0])) % 2) == (((int(a[3]) - int(a[1])) // int(b[1])) % 2)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
