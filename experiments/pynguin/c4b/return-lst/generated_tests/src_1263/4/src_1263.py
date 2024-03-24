def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = str(args[1])
	a = 0
	b = 0
	for (i, num) in enumerate(s):
	    if ((num != '7') and (num != '4')):
	        ret_values.append('NO')
	        a = (- 1)
	        b = (- 2)
	        break
	    elif ((i + 1) <= (n / 2)):
	        a += int(num)
	    else:
	        b += int(num)
	else:
	    if (a == b):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
