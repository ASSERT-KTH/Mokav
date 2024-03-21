def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	cnt = 1
	while 1:
	    if (cnt & 1):
	        a -= cnt
	    else:
	        b -= cnt
	    if (a < 0):
	        ret_values.append('Vladik')
	        quit()
	    elif (b < 0):
	        ret_values.append('Valera')
	        quit()
	    else:
	        cnt += 1

	return ret_values
