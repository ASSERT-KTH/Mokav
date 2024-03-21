def func(*args):
	ret_values = []
	
	a = list(map(int, args[0].split(' ')))
	if (((abs((a[0] - a[1])) == 1) or ((a[0] - a[1]) == 0)) and (((a[0] > 0) and (a[1] == 0)) or ((a[0] == 0) and (a[1] > 0)) or ((a[0] > 0) and (a[1] > 0)))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
