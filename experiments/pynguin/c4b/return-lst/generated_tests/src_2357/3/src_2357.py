def func(*args):
	ret_values = []
	
	K = int(args[0])
	L = int(args[1])
	importance = 0
	flag = 0
	for i in range(1, 65):
	    if ((K ** i) == L):
	        flag = 1
	        importance = i
	        break
	if (flag == 1):
	    ret_values.append('YES')
	    ret_values.append((importance - 1))
	else:
	    ret_values.append('NO')

	return ret_values
