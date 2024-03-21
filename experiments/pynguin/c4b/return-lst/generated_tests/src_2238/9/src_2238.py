def func(*args):
	ret_values = []
	
	flag = 0
	str = args[0]
	a = ['H', 'Q', '9']
	for i in str:
	    if (i in a):
	        flag = 1
	if (flag == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
