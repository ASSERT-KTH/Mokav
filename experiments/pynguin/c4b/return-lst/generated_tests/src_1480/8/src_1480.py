def func(*args):
	ret_values = []
	
	s = args[0]
	li = ['H', 'Q', '9']
	flag = True
	for i in li:
	    if (i in s):
	        ret_values.append('YES')
	        flag = False
	        break
	if flag:
	    ret_values.append('NO')

	return ret_values
