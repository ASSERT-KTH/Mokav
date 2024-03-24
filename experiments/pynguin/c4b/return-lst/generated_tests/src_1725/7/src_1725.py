def func(*args):
	ret_values = []
	
	n = int(args[0])
	num = args[1]
	flag = 0
	for i in num:
	    if ((i < '4') or ('4' < i < '7') or (i > '7')):
	        ret_values.append('NO')
	        flag = 1
	        break
	if (flag == 0):
	    if (sum(map(int, num[:(n // 2)])) == sum(map(int, num[(n // 2):]))):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
