def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	cnt = 1
	while True:
	    if ((cnt % 2) == 1):
	        a -= cnt
	    else:
	        b -= cnt
	    if (b < 0):
	        ret_values.append('Valera')
	        break
	    if (a < 0):
	        ret_values.append('Vladik')
	        break
	    cnt += 1

	return ret_values
