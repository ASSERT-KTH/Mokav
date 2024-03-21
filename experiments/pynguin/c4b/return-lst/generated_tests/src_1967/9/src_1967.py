def func(*args):
	ret_values = []
	
	a = args[0]
	x = list()
	flag = 0
	for i in range(0, len(a)):
	    if ((a[i] == '4') or (a[i] == '7')):
	        flag += 1
	if ((flag == 4) or (flag == 7)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
