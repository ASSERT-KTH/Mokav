def func(*args):
	ret_values = []
	
	k = int(args[0].strip())
	l = int(args[1].strip())
	jav = 0
	while True:
	    if (l == 1):
	        ret_values.append('YES')
	        ret_values.append((jav - 1))
	        break
	    elif ((l % k) == 0):
	        jav += 1
	        l = (l // k)
	    else:
	        ret_values.append('NO')
	        break

	return ret_values
