def func(*args):
	ret_values = []
	
	l = list(args[0].split())
	table = {0: 52, 1: 52, 2: 52, 3: 52, 4: 52, 5: 53, 6: 53}
	if (l[2] == 'week'):
	    ret_values.append(table[(int(l[0]) % 7)])
	else:
	    n = int(l[0])
	    if (n <= 29):
	        ret_values.append(12)
	    elif (n > 30):
	        ret_values.append(7)
	    else:
	        ret_values.append(11)

	return ret_values
