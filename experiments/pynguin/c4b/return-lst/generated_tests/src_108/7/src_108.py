def func(*args):
	ret_values = []
	
	a = args[0]
	num = (a.count('4') + a.count('7'))
	num = str(num)
	if (len(num) == (num.count('4') + num.count('7'))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
