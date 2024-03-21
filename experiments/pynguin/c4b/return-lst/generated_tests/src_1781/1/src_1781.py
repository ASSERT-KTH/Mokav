def func(*args):
	ret_values = []
	
	n = int(args[0])
	l = [0, 8, 16, 24, 4, 12, 20]
	flag = 0
	for i in range(7):
	    if (((n % 7) == i) and (n >= l[i])):
	        n -= l[i]
	        k = (n // 7)
	        p = (l[i] // 4)
	        flag = 1
	        break
	if (flag == 0):
	    ret_values.append((- 1))
	else:
	    for i in range(p):
	        ret_values.append(4, end='')
	    for i in range(k):
	        ret_values.append(7, end='')

	return ret_values
