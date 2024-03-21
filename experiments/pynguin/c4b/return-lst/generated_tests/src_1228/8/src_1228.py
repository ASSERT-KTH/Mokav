def func(*args):
	ret_values = []
	
	str = args[0].split()
	a = int(str[0])
	b = int(str[1])
	count = 0
	if (a == b):
	    ret_values.append('1')
	else:
	    while (a <= b):
	        a = (a * 3)
	        b = (b * 2)
	        count += 1
	    ret_values.append(count)

	return ret_values
